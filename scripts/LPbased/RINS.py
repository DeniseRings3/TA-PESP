import utils.auswertung as util
import LPbased.sort_alternatives_improvement as sort
import LPbased.LPmodel as lp
import analyse_results.evaluate_solutions_functions as ev
import utils.analyse_log as log
import build_ean.read_entire_input as ri
import param as param
import timeit
import datetime
import os

# Configurations
path = r'/Users/deniserings/Documents/zib/s-bahn-data/processed/'
#path = r'/data/optimi/optimi/kombadon/drings/SBahn/s-bahn-data/processed/'
#out_path = r'/data/optimi/optimi/kombadon/drings/SBahn/s-bahn-data/scripts/DeniseMA/processed/'
out_path = r'/Users/deniserings/Documents/zib/s-bahn-data/scripts/DeniseMA/processed/'

zugfolge = param.zugfolge
epsilon = param.epsilon
T = param.T
custom_time = param.custom_time
# current configuration
all_models = param.all_models

timeout = param.timeout
feasibility_stop = param.feasibility_stop
feasibility_time_limit = param.feasibility_time_limit
results_file = out_path + param.results_file
#r_i = param.fixed_integer_ratio
relaxed = param.rins_relax
ratios = param.ratios_relax


timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
timestamp_file = datetime.datetime.now().strftime("%Y%m%d%H%M")
print(timestamp_file)

rins_epsilon = param.rins_epsilon
comment = 'standard RINS, inequality'

semicolon = ['BBER_BBU','BBUP_O','BBUP_W','BPKW_BKRW_BSNF_O', 'BWKS_medium_september']
mip_start_sol_dict = {}
lp_opt_sol_dict = {}



for modelname in all_models:
    filename = out_path  +'final/StartSol/'+ modelname +'/' + modelname + '_202403291817_RINSstart.sol'
    sol_new, objective = ev.read_solution_file(filename)
    mip_start_sol_dict[modelname] = sol_new

    filename = out_path + '/final/LPRelaxation_ineq/'+modelname+'/'+ modelname+'_lp.sol'
    sol_new, objective = ev.read_solution_file(filename)
    lp_opt_sol_dict[modelname] = sol_new




for modelname in all_models:
    print(modelname)
    model_path = path + 'Denise_instances/' + modelname +'/'
    model_out_path = out_path + modelname + '/RINS/'

    if modelname in semicolon:
        sep = ';'
    else:
        sep = ','

    # read input
    ean, ean_noH, curly_H, sheaf_dict, alternatives_dict = ri.read_input(model_path, modelname, T, epsilon, zugfolge, sep)

    for F in alternatives_dict:
        if F not in mip_start_sol_dict[modelname]['b']:
            mip_start_sol_dict[modelname]['b'][F] = 0

    # clean log files
    filename = model_out_path+ modelname+'_'+ timestamp_file+'_'
    param.write_config(filename)
    try:
        os.remove(filename + '.log')
    except OSError:
        pass

    # ratio of fixed integral variables
    start = timeit.default_timer()
    fixed_sheaves = []
    fixed_alternatives = 0
    equality_set = []
    for F in alternatives_dict.keys():
        if lp_opt_sol_dict[modelname]['b'][F] == mip_start_sol_dict[modelname]['b'][F]:
            if lp_opt_sol_dict[modelname]['b'][F]  == 1:
                equality_set.append(F)
                sheaf = alternatives_dict[F]['sheaf_idx']
                fixed_sheaves.append(sheaf)
                fixed_alternatives += len(sheaf_dict[sheaf])

    relaxations = []
    if relaxed:
        # try different relaxations

        for ratio in ratios:
            # 1: random

            for i in range(5):
                fixed_subset = sort.random_selection(equality_set, ratio, alternatives_dict, sheaf_dict)
                relaxations.append(('random'+str(i), ratio, fixed_subset))

            # 2
            # sort by anzahl ausgeschlossener alternativen
            non_fixed_subset = sort.sorted_by_excluded_alternatives(equality_set, ratio, alternatives_dict,
                                                                    sheaf_dict)
            relaxations.append(('other alternatives', ratio, non_fixed_subset))

            # sort by slack

            fixed_subset = sort.sort_by_slack(alternatives_dict, lp_opt_sol_dict[modelname], ratio, ean, equality_set)
            relaxations.append(('slack', ratio, fixed_subset))

    else:
        relaxations.append(('no relaxation', 1, equality_set))

    equality_ratio = len(equality_set)/len(list(alternatives_dict.keys()))



    for (type, ratio, fixed_subset) in relaxations:
        print((type, ratio))
        filename = model_out_path + modelname + '_' + timestamp_file + '_'
        filename += type+'_'+str(ratio)
        m,p,pi,y,y_bar,h,b = lp.RINS_subMIP(modelname, ean, alternatives_dict, T, epsilon, zugfolge, curly_H,
                                         sheaf_dict,
                                       lp_opt_sol_dict[modelname],mip_start_sol_dict[modelname], equality_set, rins_epsilon,
                                       model_out_path, timeout= timeout, sol = mip_start_sol_dict[modelname],
                                            filename=filename,relaxed = True,
                                            feasibility_stop = False, feasibility_time_limit = 2,
                                            no_improvement_stop = True,
                                            fixed_subset = fixed_subset)
        #, non_fixed_subset = non_fixed_subset


        print('model status',m.status, m.status == 3)
        if m.status == 3 or m.SolCount < 1: # GRB.INFEASIBLE
            # print('in if')
            rins_solvable = False
            rins_gap = '-'
            rins_objective = '-'
            rins_time = '-'
            time_out = False
            feasibility_check = False
            first_sol_time = -1
            first_sol_obj = -1
            first_sol_gap = -1
            # custom_time = -1
            custom_time_obj = -1
            custom_time_gap = -1
            postprocessing_time = 0

            plat_index = -1
            plat_time = -1
            plat_obj = -1
            plat_gap = -1
        else:
            rins_solvable = True


            # test if solution is feasible
            start = timeit.default_timer()
            table, time_out, rins_objective, bound, rins_gap, time, solution_count, solve_interrupted = log.evaluate_log(
                filename + '.log')

            sol_file = filename + '.sol'
            sol, objective = ev.read_solution_file(sol_file)

            # check solution:
            activated_edges = [(i, j) for F in alternatives_dict for (i, j) in alternatives_dict[F]['path'] if
                               sol['b'][F] == 1]
            non_activated_edges_1 = [(i, j) for (i, j) in ean_noH.edges if
                                     sol['h'][(i, j)] == 1 and (i, j) not in activated_edges]
            print('non activated edges that are 1', non_activated_edges_1)
            surplus_edges = len(non_activated_edges_1)

            for (i, j) in non_activated_edges_1:
                print(i, j, ean[i][j])
                sol['h'][(i, j)] = 0
            stop = timeit.default_timer()
            postprocessing_time = stop - start

            m, p, pi, y, y_bar, h, b = bd.set_up_model(modelname, ean, alternatives_dict, 200, epsilon, zugfolge,
                                                       curly_H,
                                                       sheaf_dict, model_out_path, feasibility_stop=True,
                                                       feasibility_time_limit=2, sol=sol, test_start=True,
                                                       filename=filename + '_test', timeout = 2)
            if m.status == GRB.INFEASIBLE:
                print('not a solution')
                feasibility_check = False
            else:
                print('found a feasible solution')
                feasibility_check = True


            log_dict = log.create_log_dict(table, detailed=True)
            log_dict['Incumbent'] = util.no_solution_substitute(log_dict['Incumbent'], -100)
            first_sol_index, first_sol_time, first_sol_obj, first_sol_gap = util.get_first_sol(log_dict)
            custom_time_cutoff_index, custom_time_obj, custom_time_gap = util.get_sol_custom_time_cutoff(log_dict,
                                                                                                         custom_time)
            plat_index, plat_time, plat_obj, plat_gap = util.get_first_occ_of_plateau_sol(log_dict,
                                                                                          log_dict['Incumbent'][-1])

        # else:
    #     print('not enough variables fixed ')
    #     comment = 'not enough variables fixed'
    #     rins_solvable = False
    #     rins_solvable = False
    #     rins_gap = '-'
    #     rins_objective = '-'
    #     rins_time = '-'

        stop = timeit.default_timer()
        rins_time = stop - start



        header = ['Model', 'filename','comment', 'date', 'time', 'timeout', 'gap in %', 'objective',
                  'fixed integer values ratio', 'solvable', 'relaxed', 'ratio', 'type' ,'feasibility check',
                  'postprocessing'
                  'first_sol_time', 'first_sol_obj',
                  'first_sol_gap',
                     'plateau_time', 'plateau_time_obj', 'plateau_time_gap'
                  ]

        filename_short = modelname + '_subMBP_' + timestamp_file
        row = [modelname,filename_short, comment, timestamp, rins_time, time_out, rins_gap, rins_objective,
               equality_ratio, rins_solvable, True, ratio, type, feasibility_check,
               postprocessing_time,
               first_sol_time, first_sol_obj, first_sol_gap,
               plat_time, plat_obj, plat_gap]


        log.write_detailed_results_excel(results_file, header, row, create_new_file=False)



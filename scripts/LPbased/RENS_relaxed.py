from gurobipy.gurobipy import GRB
import build_ean.read_entire_input as ri
import utils.analyse_log as log
from utils.auswertung import *
import LPbased.LPmodel as lp
import LPbased.sort_alternatives_improvement as sort
import model.BuildModel as bd
import build_ean.read_ean_functions as rd
import timeit
import datetime
import utils.auswertung as util
import param as param


# Configurations
path = param.path
out_path = param.out_path
zugfolge = param.zugfolge
epsilon = param.epsilon
T = param.T
custom_time = param.custom_time
path = r'/Users/deniserings/Documents/zib/s-bahn-data/processed/'
out_path = r'/Users/deniserings/Documents/zib/s-bahn-data/scripts/DeniseMA/processed/'

# current configuration
all_models = param.all_models

timeout = param.timeout
feasibility_stop = param.feasibility_stop
feasibility_time_limit = param.feasibility_time_limit
results_file = out_path + param.results_file
r_i = param.fixed_integer_ratio
ratios = param.ratios_relax

comment = 'multiple_random_values'
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
timestamp_file = datetime.datetime.now().strftime("%Y%m%d%H%M")
print(timestamp_file)

#######################################################################################################################

semicolon = ['BBER_BBU', 'BBUP_O', 'BBUP_W',
             'BPKW_BKRW_BSNF_O', 'BWKS_medium_september']
# current configuration

optimal_sol = defaultdict(lambda:[])
for modelname in all_models:
    filename = r'/Users/deniserings/Documents/zib/s-bahn-data/scripts/DeniseMA/processed/final/LPRelaxation_ineq/' + \
               modelname + '/' + modelname + '_lp.sol'

    sol_og, objective = ev.read_solution_file(filename)
    optimal_sol[modelname] = sol_og

comment = 'random'
#
for modelname in all_models:
    print(modelname)
    model_path = path + 'Denise_instances/' + modelname + '/'
    model_out_path = out_path + modelname + '/original/LP_based/'

    if modelname in semicolon:
        sep = ';'
    else:
        sep = ','

    # read input
    ean, ean_noH, curly_H, sheaf_dict, alternatives_dict = ri.read_input(model_path, modelname, T, epsilon, zugfolge,
                                                                         sep)


    filename = model_out_path + modelname
    print(filename)
    # read LP relaxation solution
    sol_file = out_path+'final/LPRelaxation_ineq/' + \
               modelname + '/' + modelname + '_lp.sol'
    lp_relax_sol, objective = read_solution_file(sol_file)
    print('lp solution')

    integral = []
    fractional = []

    start = timeit.default_timer()
    lp_opt = {}

    for F in lp_relax_sol['b']:
        lp_opt[F] = lp_relax_sol['b'][F]
        frac =lp_opt[F] - int(lp_opt[F])
        if frac == 0:
            integral.append(F)
        else:
            fractional.append(F)


    b = lp_relax_sol['b']
    lp_relaxation_time = 'presolved'
    fixed = len(integral)

    fixed_integer_ratio = fixed / len(b.values())
    comment = ' '
    if fixed >= r_i * len(b.values()):

        # try different relaxations
        relaxations = []

        filepath = out_path + modelname + '/RENS/'

        for ratio in ratios:
            integer_values = [F for F in lp_opt if (lp_opt[F] == 0 or lp_opt[F] == 1)]
            # 1: random
            for i in range(5):
                fixed_subset = sort.random_selection(integer_values, ratio, alternatives_dict, sheaf_dict)
                relaxations.append(('random'+str(i), ratio, fixed_subset))

            # # 2
            # sort by anzahl ausgeschlossener alternativen

            fixed_subset = sort.sorted_by_excluded_alternatives(integer_values, ratio, alternatives_dict,
                                                                    sheaf_dict)
            relaxations.append(('other alternatives', ratio, fixed_subset))

            # sort by slack
            fixed_subset = sort.sort_by_slack(alternatives_dict, lp_relax_sol, ratio,ean)
            relaxations.append(('slack', ratio, fixed_subset))
            print('slack', fixed_subset)


        for (type, ratio, fixed_subset) in relaxations:
            print((type, ratio, fixed_subset))
            filename = filepath+ modelname + '_subMBP_' + type + '_' + str(ratio) + '_' + timestamp_file
            m, p, pi, y, y_bar, h, b = lp.subMIP(modelname, ean, alternatives_dict, T, epsilon, zugfolge, curly_H,
                                                 sheaf_dict, lp_opt, model_out_path, timeout= timeout ,
                                                 feasibility_stop=False, feasibility_time_limit=2,
                                                 no_improvement_stop = True,
                                                 fixed_subset=fixed_subset,
                                                 filename=filename,
                                                 relaxed = True)

            if m.status == GRB.INFEASIBLE or m.SolCount < 1:
                rens_solvable = False
                rens_gap = '-'
                rens_objective = '-'
                rens_time = '-'
                time_out = False
                feasibility_check  = False
                first_sol_time = -1
                first_sol_obj = -1
                first_sol_gap = -1
                custom_time = -1
                custom_time_obj = -1
                custom_time_gap = -1
                plat_index = -1
                plat_time = -1
                plat_obj = -1
                plat_gap = -1
            else:
                rens_solvable = True
                table, time_out, rens_objective, bound, rens_gap, time, solution_count, solve_interrupted = log.evaluate_log(
                    filename + '.log')

                log_dict = log.create_log_dict(table, detailed=True)
                log_dict['Incumbent'] = util.no_solution_substitute(log_dict['Incumbent'], -100)
                first_sol_index, first_sol_time, first_sol_obj, first_sol_gap = util.get_first_sol(log_dict)
                custom_time_cutoff_index, custom_time_obj, custom_time_gap = util.get_sol_custom_time_cutoff(log_dict,
                                                                                                             custom_time)

                plat_index, plat_time, plat_obj, plat_gap = util.get_first_occ_of_plateau_sol(log_dict,
                                                                                              log_dict['Incumbent'][-1])

                # test if solution is feasible
                sol_file = filename + '.sol'
                sol, objective = read_solution_file(sol_file)

                # postprocessing
                activated_edges = [(i, j) for F in alternatives_dict for (i, j) in alternatives_dict[F]['path'] if
                                   sol['b'][F] == 1]
                non_activated_edges_1 = [(i, j) for (i, j) in ean_noH.edges if
                                         sol['h'][(i, j)] == 1 and (i, j) not in activated_edges]
                print('non activated edges that are 1', non_activated_edges_1)
                surplus_edges = len(non_activated_edges_1)

                for (i, j) in non_activated_edges_1:
                    print(i, j, ean[i][j])
                    sol['h'][(i, j)] = 0


                m, p, pi, y, y_bar, h, b = bd.set_up_model(modelname, ean, alternatives_dict, 200, epsilon, zugfolge,
                                                           curly_H,
                                                           sheaf_dict, model_out_path,
                                                           timeout = 2,feasibility_stop=True,
                                                           feasibility_time_limit=2, sol=sol, test_start=True,
                                                           filename=filename + '_test')
                if m.status == GRB.INFEASIBLE:
                    print('not a solution')
                    feasibility_check = False
                else:
                    print('found a feasible solution')
                    feasibility_check = True



            stop = timeit.default_timer()
            filename = modelname + '_subMBP_' + type + '_' + str(ratio) + '_' + timestamp_file
            rens_time = stop - start

            header = ['Model', 'comment', 'filename', 'date', 'time', 'timeout', 'gap in %', 'objective',
                      'fixed integer values ratio', 'solvable', 'relaxed', 'ratio','type' ,'feasibility check',
                      'first_sol_time', 'first_sol_obj', 'first_sol_gap',
                       'plateau_time', 'plateau_time_obj', 'plateau_time_gap'
                      ]

            filename_short = modelname + '_subMBP_' + timestamp_file
            row = [modelname, comment, filename_short, timestamp, rens_time, time_out, rens_gap, rens_objective,
                   fixed_integer_ratio, rens_solvable, False, ratio,type, feasibility_check,
                   first_sol_time, first_sol_obj, first_sol_gap,
                   plat_time, plat_obj, plat_gap]

            log.write_detailed_results_excel(results_file, header, row, create_new_file=False)



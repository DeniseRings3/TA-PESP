from gurobipy.gurobipy import GRB
import build_ean.read_entire_input as ri
import utils.analyse_log as log
from analyse_results.evaluate_solutions_functions import  *
import LPbased.LPmodel as lp
import model.BuildModel as bd
import timeit
import datetime
import utils.auswertung as util
import param as param

# Configurations
path = param.path
out_path = param.out_path

path = r'/Users/deniserings/Documents/zib/s-bahn-data/processed/'
out_path = r'/Users/deniserings/Documents/zib/s-bahn-data/scripts/DeniseMA/processed/'

zugfolge =  param.zugfolge
epsilon = param.epsilon
T =  param.T
custom_time = param.custom_time

# current configuration
all_models = param.all_models

timeout = param.timeout
feasibility_stop = param.feasibility_stop
feasibility_time_limit = param.feasibility_time_limit
results_file = out_path + param.results_file
r_i = param.fixed_integer_ratio



timestamp =  datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
timestamp_file = datetime.datetime.now().strftime("%Y%m%d%H%M")
print(timestamp_file)


#######################################################################################################################

semicolon = ['BBER_BBU','BBUP_O','BBUP_W',
              'BPKW_BKRW_BSNF_O', 'BWKS_medium_september']
# current configuration

comment = ''

for modelname in all_models:
    print(modelname)
    model_path = path + 'Denise_instances/' + modelname +'/'
    model_out_path = out_path + modelname + '/original/LP_based/'

    if modelname in semicolon:
        sep = ';'
    else:
        sep = ','

    # read input
    print(model_path)
    ean, ean_noH, curly_H, sheaf_dict, alternatives_dict = ri.read_input(model_path, modelname, T, epsilon, zugfolge, sep)

    # # clean log files
    filename = model_out_path+ modelname
    param.write_config(filename)

    # read LP relaxation solution
    sol_file = r'/Users/deniserings/Documents/zib/s-bahn-data/scripts/DeniseMA/processed/final/LPRelaxation_ineq/'+\
               modelname+'/'+ modelname+'_lp.sol'

    sol, objective = read_solution_file(sol_file)


    integral = []
    fractional = []

    start = timeit.default_timer()
    lp_opt = {}

    for F in sol['b']:
        lp_opt[F] = sol['b'][F]
        frac = sol['b'][F] - int(sol['b'][F])
        if frac == 0:
            integral.append(F)
        else:
            fractional.append(F)

    b = sol['b']
    lp_relaxation_time = 'presolved'
    fixed = len(integral)

    fixed_integer_ratio = fixed/len(b.values())
    comment = ' '
    if fixed >= r_i * len(b.values()):
        filename = out_path + modelname + '/RENS/'+ modelname + '_subMBP_' + timestamp_file


        integer_values = [F for F in lp_opt if (lp_opt[F] == 0 or lp_opt[F] == 1)]

        m,p,pi,y,y_bar,h,b = lp.subMIP(modelname, ean, alternatives_dict, T, epsilon, zugfolge, curly_H,
                                             sheaf_dict, lp_opt, model_out_path, timeout= timeout,
                   feasibility_stop=feasibility_stop, feasibility_time_limit=2,
                                           filename= filename, relaxed = True ,
                                       fixed_subset = integer_values,
                                       no_improvement_stop = True)
        stop = timeit.default_timer()
        if m.status == GRB.INFEASIBLE or m.SolCount < 1:
            rens_solvable = False
            rens_gap = '-'
            rens_objective = '-'
            rens_time = '-'
            feasibility_check = False
            time_out = False
            first_sol_time = -1
            first_sol_obj = -1
            first_sol_gap = -1
            #custom_time = -1
            custom_time_obj = -1
            custom_time_gap = -1

            plat_index = -1
            plat_time = -1
            plat_obj = -1
            plat_gap = -1
        else:
            rens_solvable = True
            table, time_out, rens_objective, bound, rens_gap, time, solution_count, solve_interrupted = log.evaluate_log(
                filename+ '.log')

            # test if solution is feasible
            sol_file = filename + '.sol'
            sol, objective = read_solution_file(sol_file)
            m, p, pi, y, y_bar, h, b = bd.set_up_model(modelname, ean, alternatives_dict, T, epsilon, zugfolge,
                                                       curly_H,
                                                       sheaf_dict, model_out_path, timeout = 2,
                                                       feasibility_stop=True,
                                                       feasibility_time_limit=2, sol=sol, test_start=True,
                                                       filename=filename + '_test')
            if m.status == GRB.INFEASIBLE:
                print('not a solution')
                feasibility_check = False
            else:
                print('found a feasible solution')
                feasibility_check = True

            table, time_out, objective, bound, gap, time, solution_count, solve_interrupted = log.evaluate_log(filename+'.log')
            log_dict = log.create_log_dict(table, detailed=True)
            log_dict['Incumbent'] = util.no_solution_substitute(log_dict['Incumbent'], -100)
            first_sol_index, first_sol_time, first_sol_obj, first_sol_gap = util.get_first_sol(log_dict)
            custom_time_cutoff_index, custom_time_obj, custom_time_gap = util.get_sol_custom_time_cutoff(log_dict,
                                                                                                         custom_time)

            plat_index, plat_time, plat_obj, plat_gap = util.get_first_occ_of_plateau_sol(log_dict,
                                                                                          log_dict['Incumbent'][-1])



    else:
        print('not enough variables fixed ')
        comment = 'not enough variables fixed'
        rens_solvable = False
        rens_solvable = False
        rens_gap = '-'
        rens_objective = '-'
        rens_time = '-'
        feasibility_check = False
        time_out = False
        stop = timeit.default_timer()
        first_sol_time = -1
        first_sol_obj =-1
        first_sol_gap = -1
        #custom_time = -1
        custom_time_obj = -1
        custom_time_gap = -1

        plat_index= -1
        plat_time = -1
        plat_obj = -1
        plat_gap =-1


    rens_time = stop - start


    header = ['Model','comment','filename','date','time','timeout','gap in %','objective',
              'fixed integer values ratio', 'solvable','relaxed', 'feasibility check',
              'first_sol_time', 'first_sol_obj', 'first_sol_gap',
              'plateau_time', 'plateau_time_obj', 'plateau_time_gap'
              ]

    filename_short =  modelname + '_subMBP_' + timestamp_file
    row = [modelname,comment, filename_short,timestamp, rens_time, time_out, rens_gap,rens_objective,
           fixed_integer_ratio,rens_solvable,False,feasibility_check,
           first_sol_time, first_sol_obj, first_sol_gap,
           plat_time, plat_obj, plat_gap]

    log.write_detailed_results_excel(results_file, header, row,create_new_file=False)



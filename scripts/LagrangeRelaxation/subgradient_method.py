from gurobipy.gurobipy import GRB
import analyse_results.evaluate_solutions_functions as ev
import model.BuildModel as bd
import build_ean.read_entire_input as ri

from analyse_results.evaluate_solutions_functions import *
import LagrangeRelaxation.subgradient_functions as sub
import utils.analyse_log as log
import param as param
import timeit
import datetime

# Configurations
path = param.path
out_path = param.out_path
zugfolge = param.zugfolge
epsilon = param.epsilon
T = param.T

path = r'/Users/deniserings/Documents/zib/s-bahn-data/processed/'
out_path = r'/Users/deniserings/Documents/zib/s-bahn-data/scripts/DeniseMA/processed/'

# current configuration
all_models = param.all_models

timeout = param.timeout
feasibility_stop = param.feasibility_stop
feasibility_time_limit = param.feasibility_time_limit
results_file = out_path + param.results_file
max_iterations = param.max_iter
c_k = param.c_k
type_sheaf =  param.type_sheaf
type_activation = param.type_activation
overall_timeout = param.overall_timeout


timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
timestamp_file = datetime.datetime.now().strftime("%Y%m%d%H%M")
print(timestamp_file)

timeout= 3

Z_star_type = 'LP'
feasibility_stop= False
c_k_dynamic = True
gap_stop = True
time_limit_after_callback = 10
time_out_per_iteration = 5*60
overall_time_out = 10 *60
hard_fix = False
hard_fix_relaxation_Ratio = 1
max_iterations = 40

comment = 'gapstop, 5sec'
##################################################################


semicolon = ['BBER_BBU','BBUP_O','BBUP_W',
              'BPKW_BKRW_BSNF_O', 'BWKS_medium_september']


mip_start_sol_dict = defaultdict(lambda:defaultdict(lambda:[]))
lp_opt_sol_dict = defaultdict(lambda:defaultdict(lambda:[]))


running_time = overall_time_out
for modelname in all_models:
    filename = out_path + modelname + '/original/LP_based/' + modelname + '_b_continuous_h_continuous.sol'
    sol_new, objective = ev.read_solution_file(filename)
    lp_opt_sol_dict[modelname]['x'] = sol_new
    lp_opt_sol_dict[modelname]['objective'] = objective

# subgradient

for modelname in all_models:
    print(modelname)
    print(modelname)
    model_path = path + 'Denise_instances/' + modelname +'/'
    model_out_path = out_path + modelname + '/original/LP_based/'

    if modelname in semicolon:
        sep = ';'
    else:
        sep = ','

    # read input
    ean, ean_noH, curly_H, sheaf_dict, alternatives_dict = ri.read_input(model_path, modelname, T, epsilon, zugfolge, sep)

    print('edges', len(ean.edges()), 0.005 * len(ean.edges()))

    # clean log files
    filename = model_out_path + modelname + '_subgradient_' + timestamp_file # '_b_'+type_b+'_h_'+type_h

    # write config stuff
    header = ['Model', 'timestamp','c_k', 'Z_star_type', 'feasibility_stop', 'c_k_dynamic', 'gap_stop', 'time_limit_after_callback',
              'time_out_per_iteration',
    'overall_time_out', 'hard_fix', 'hard_fix_relaxation_Ratio','max_iterations' ]
    row = [modelname,timestamp,c_k, Z_star_type, feasibility_stop, c_k_dynamic, gap_stop, time_limit_after_callback,time_out_per_iteration,
    overall_time_out, hard_fix, hard_fix_relaxation_Ratio,max_iterations ]

    log.write_detailed_results_excel(filename + '_config.csv', header, row, create_new_file=False)

    if type_activation:
        filename += 'act_'
    if type_sheaf:
        filename += 'sheaf'

    param.write_config(filename)
    try:
        os.remove(filename + '.log')
    except OSError:
        pass

    start = timeit.default_timer()

    # input:

    Z_star = lp_opt_sol_dict[modelname]['objective']

    lambda_0 ={}
    if type_sheaf:
        for sheaf in sheaf_dict:
            lambda_0[sheaf] = 0 # or min of cost

    if type_activation:
        for (i,j) in ean_noH.edges():
            lambda_0[(i,j)] = ean_noH[i][j]['w']

    # start with lp solution

    sol, objective, abbruch, iterations = sub.subgradient(modelname, ean, ean_noH, alternatives_dict, T, epsilon,zugfolge,
                                                          curly_H, sheaf_dict, filename,timeout,
                   lambda_0,max_iterations,c_k,type_sheaf, type_activation, Z_star, timestamp_file,
                                                          overall_time_out,model_out_path,
                                                          start_sol = lp_opt_sol_dict[modelname],
                                                          c_k_dynamic= c_k_dynamic,
                                                          #####
                                                          gap_stop= True, time_limit_after_callback= time_limit_after_callback,
                                                          time_out_per_iteration= time_out_per_iteration,
                                                          overall_time_out= overall_time_out,
                                                          hard_fix= hard_fix,
                                                          hard_fix_relaxation_Ratio= hard_fix_relaxation_Ratio)

    stop = timeit.default_timer()
    if sol == 'no solution':
        comment = 'no relaxed solution found'
        feasibility_check = False
        gap = '-'
        objective = 0

    if sol == {}:
        print('there is a problem')
        feasibility_check = False
        gap = '-'

        objective = 0
    else:
        # test if solution is feasible
        table, time_out, objective_test, bound, gap, time, solution_count, solve_interrupted = log.evaluate_log(
            filename + '.log')
        # check solution:
        activated_edges = [(i, j) for F in alternatives_dict for (i, j) in alternatives_dict[F]['path'] if
                           sol['b'][F] == 1]
        non_activated_edges_1 = [(i, j) for (i, j) in ean_noH.edges if
                                 sol['h'][(i, j)] == 1 and (i, j) not in activated_edges]
        for (i,j) in non_activated_edges_1:
            sol['h'][(i, j)] = 0


        m, p, pi, y, y_bar, h, b = bd.set_up_model(modelname, ean, alternatives_dict, 200, epsilon, zugfolge,
                                                           curly_H,
                                                           sheaf_dict, model_out_path,
                                                   timeout= 1,
                                                   feasibility_stop=True,
                                                       feasibility_time_limit=2, sol=sol, test_start=True,
                                                   filename=filename+'_test')

        table, original_time_out, original_objective, bound, original_gap, time, solution_count, solve_interrupted = log.evaluate_log(
            filename + '.log')

        if m.status == GRB.INFEASIBLE or m.SolCount < 1:
            print('not a solution')
            original_objective = -1
            feasibility_check = False
        else:
            print('found a feasible solution')
            feasibility_check = True



    lagrange_relaxation_time = stop - start

    header = ['Model', 'comment', 'filename', 'date', 'time', 'timeout', 'gap in %', 'objective',
              'sheaf relaxation','activation relaxation','feasibility check', 'feasibility_stop','total timeout', '#iterations']

    filename_short = modelname + '_subgradient_'  # '_b_'+type_b+'_h_'+type_h

    if type_activation:
        filename_short += 'act_'

    if type_sheaf:
        filename_short += 'sheaf'


    row = [modelname, comment,filename_short,timestamp, round(lagrange_relaxation_time,2),abbruch,
           original_gap,round(original_objective,2),
           type_sheaf,type_activation,feasibility_check,
           feasibility_stop, timeout, iterations
           ]

    log.write_detailed_results_excel(results_file, header, row, create_new_file=False)


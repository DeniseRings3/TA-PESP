import model.BuildModel as bd
import os
import utils.analyse_log as log
import utils.auswertung as ev
import build_ean.read_entire_input as ri
import utils.auswertung as util
import timeit
import datetime
from gurobipy.gurobipy import GRB

import param as param

path = r'/Users/deniserings/Documents/zib/s-bahn-data/processed/'
out_path = r'/Users/deniserings/Documents/zib/s-bahn-data/scripts/DeniseMA/processed/'

zugfolge =  param.zugfolge
epsilon = param.epsilon
T =  param.T


# current configuration
all_models = param.all_models

timeout = param.timeout
feasibility_stop = param.feasibility_stop
feasibility_time_limit = param.feasibility_time_limit
results_file = out_path + param.results_file

comment = 'coupling constraint as inequality'
timestamp =  datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
timestamp_file = datetime.datetime.now().strftime("%Y%m%d%H%M")
custom_time = param.custom_time
print(timestamp_file)


#######################################################################################################################

semicolon = ['BBER_BBU','BBUP_O','BBUP_W',
              'BPKW_BKRW_BSNF_O', 'BWKS_medium_september']


for modelname in all_models:
    print(modelname)

    model_path = path + 'Denise_instances/' + modelname +'/'
    model_out_path = out_path + modelname + '/original/'

    filename = out_path + modelname + '/RENS/' + modelname + '_subMBP.sol'
    mip_start, mip_objective = ev.read_solution_file(filename)

    # try with start solution
    filename = out_path  +'final/StartSol/'+ modelname +'/' + modelname + '_202403291817_RINSstart.sol'
    start_sol, objective = ev.read_solution_file(filename)

    if modelname in semicolon:
        sep = ';'
    else:
        sep = ','

    # read input
    ean, ean_noH, curly_H, sheaf_dict, alternatives_dict = ri.read_input(model_path, modelname, T, epsilon, zugfolge, sep)

    # clean log files
    filename = model_out_path+ modelname +'_'+timestamp_file+'_start_sol'
    param.write_config(filename )
    try:
        os.remove(filename + '.log')
    except OSError:
        pass

    start = timeit.default_timer()
    m,p,pi,y,y_bar,h,b = bd.set_up_model(modelname, ean, alternatives_dict, T, epsilon, zugfolge, curly_H, sheaf_dict,
                 out_path,timeout = timeout,
                 feasibility_stop = False, feasibility_time_limit = 2,
                 sol = start_sol,
                 no_improvement_stop=True,
                 test_start = False, filename = filename, relaxed=True)


    stop = timeit.default_timer()
    total_time = stop - start

    if m.Status == 11:
        print('no improvement stop')
        stop_func_activated = 1
    else:
        stop_func_activated = 0

    start = timeit.default_timer()
    table, time_out, objective,bound,gap,time,solution_count, solve_interrupted = log.evaluate_log(filename + '.log')
    sol_file = filename + '.sol'
    sol, objective = ev.read_solution_file(sol_file)

    # postprocessing
    activated_edges = [(i,j)  for F in alternatives_dict for (i,j) in alternatives_dict[F]['path']  if sol['b'][F] == 1]
    non_activated_edges_1 = [(i,j) for (i,j) in ean_noH.edges if sol['h'][(i,j)] == 1 and (i,j) not in activated_edges]
    print('non activated edges that are 1', non_activated_edges_1)
    surplus_edges = len(non_activated_edges_1)

    for (i,j) in non_activated_edges_1:
        print(i,j, ean[i][j])
        sol['h'][(i,j)] = 0
    stop = timeit.default_timer()
    postprocessing_time = stop - start

    # test feasibility
    m, p, pi, y, y_bar, h, b = bd.set_up_model(modelname, ean, alternatives_dict, 200, epsilon, zugfolge,
                                               curly_H,
                                               sheaf_dict, model_out_path,
                                               timeout= 2,
                                               feasibility_stop=True,
                                               feasibility_time_limit=2, sol=sol, test_start=True,
                                               filename=filename + '_test', relaxed=False)
    if m.status == GRB.INFEASIBLE or m.SolCount < 1:
        print('not a solution')
        feasibility_check = False
    else:
        print('found a feasible solution')
        feasibility_check = True

    # read log file

    #table, time_out, objective, bound, gap, time, solution_count, solve_interrupted = log.evaluate_log(filename)
    log_dict = log.create_log_dict(table, detailed=True)
    log_dict['Incumbent'] = util.no_solution_substitute(log_dict['Incumbent'], -100)
    first_sol_index, first_sol_time, first_sol_obj, first_sol_gap = util.get_first_sol(log_dict)
    custom_time_cutoff_index, custom_time_obj, custom_time_gap = util.get_sol_custom_time_cutoff(log_dict, custom_time)

    plat_index, plat_time, plat_obj, plat_gap = util.get_first_occ_of_plateau_sol(log_dict, log_dict['Incumbent'][-1])

    filename_short = modelname + '_' + timestamp_file
    row = [modelname,comment, filename_short,timestamp,feasibility_check,surplus_edges, postprocessing_time,
           first_sol_time,first_sol_obj,first_sol_gap,
           plat_time,  objective, gap]


    header = ['Model','comment','filename','date','feasibility check','surplus edges','post processing',
              'time first sol','ojective first sol','gap first sol',
              'time last sol','ojective final sol', 'gap final sol']

    log.write_detailed_results_excel(results_file, header, row)


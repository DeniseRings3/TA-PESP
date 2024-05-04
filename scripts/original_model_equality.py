import model.BuildModel as bd
import os
import utils.analyse_log as log
import build_ean.read_entire_input as ri
import utils.auswertung as util
import timeit
import datetime

import param as param #scripts.DeniseMA.scripts.

path = r'/Users/deniserings/Documents/zib/s-bahn-data/processed/'
#path = r'/data/optimi/optimi/kombadon/drings/SBahn/s-bahn-data/processed/'
#out_path = r'/data/optimi/optimi/kombadon/drings/SBahn/s-bahn-data/scripts/DeniseMA/processed/'
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

comment = 'standard model with equality constraints'
timestamp =  datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
timestamp_file = datetime.datetime.now().strftime("%Y%m%d%H%M")
print(timestamp_file)


#######################################################################################################################

semicolon = ['BBER_BBU','BBUP_O','BBUP_W',
              'BPKW_BKRW_BSNF_O', 'BWKS_medium_september']


for modelname in all_models:
    print(modelname)
    model_path = path + 'Denise_instances/' + modelname +'/'
    model_out_path = out_path + modelname + '/original/'

    if modelname in semicolon:
        sep = ';'
    else:
        sep = ','

    # read input
    ean, ean_noH, curly_H, sheaf_dict, alternatives_dict = ri.read_input(model_path, modelname, T, epsilon, zugfolge, sep)

    # clean log files
    filename = model_out_path+ modelname +'_'+timestamp+'_equality'
    param.write_config(filename )
    try:
        os.remove(filename + '.log')
    except OSError:
        pass

    start = timeit.default_timer()

    # solve TA- PESP
    m,p,pi,y,y_bar,h,b = bd.set_up_model(modelname, ean, alternatives_dict, T, epsilon, zugfolge,
                                         curly_H, sheaf_dict,
                 out_path,timeout = timeout,
                 feasibility_stop = False, feasibility_time_limit = 1,
                 sol = {},
                 no_improvement_stop=True,
                 test_start = False,
                 filename = filename, relaxed=False)

    if m.Status == 11:
        stop_func_activated = 1
    else:
        stop_func_activated = 0


    stop = timeit.default_timer()
    total_time = stop - start

    #start = timeit.default_timer()


    filename_short = modelname + '_' + timestamp_file

    table, time_out, objective, bound, gap, time, solution_count, solve_interrupted = log.evaluate_log(
        filename + '.log')
    log_dict = log.create_log_dict(table, detailed=True)
    log_dict['Incumbent'] = util.no_solution_substitute(log_dict['Incumbent'], -100)

    first_sol_index, first_sol_time, first_sol_obj, first_sol_gap = util.get_first_sol(log_dict)
    custom_time_cutoff_index, custom_time_obj, custom_time_gap = util.get_sol_custom_time_cutoff(log_dict, custom_time)

    plat_index, plat_time, plat_obj, plat_gap = util.get_first_occ_of_plateau_sol(log_dict, log_dict['Incumbent'][-1])

    filename_short = modelname + '_' + timestamp_file
    row = [modelname, comment, filename_short, timestamp,
           first_sol_time, first_sol_obj, first_sol_gap,
           plat_time, objective, gap]


    header = ['Model', 'comment', 'filename', 'date',
              'time first sol', 'ojective first sol', 'gap first sol',
              'time last sol', 'ojective final sol', 'gap final sol']

    log.write_detailed_results_excel(results_file, header, row)




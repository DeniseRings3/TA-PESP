import build_ean.read_entire_input as ri
import utils.analyse_log as log
from analyse_results.evaluate_solutions_functions import *
import LPRelaxation.LP_relaxation_functions as LP
import utils.auswertung as util

# import scripts.DeniseMA.scripts.build_ean.read_entire_input as ri
# import scripts.DeniseMA.scripts.analyse_results.analyse_log as log
# from scripts.DeniseMA.scripts.analyse_results.evaluate_solutions_functions import *
# import scripts.DeniseMA.scripts.LPbased.LPmodel as lp
# import scripts.DeniseMA.scripts.model.BuildModel as bd
# import scripts.DeniseMA.scripts.build_ean.read_ean_functions as rd

# import scripts.DeniseMA.scripts.LPbased.LPmodel as lp

import os
# import visualisations_main as vis
# import matplotlib.pyplot as plt
# import sucsessive_planning_functions as spf

# import scripts.DeniseMA.scripts.successive_sheafs.sort_alternatives as sort_alt
# import scripts.DeniseMA.scripts.successive_sheafs.successive_sheafs_functions as ssf
# import scripts.DeniseMA.scripts.visualisations.visualisations as vis
# import scripts.DeniseMA.scripts.utils.write_timetable as util
# #import successive_sheafs.successiveSheafs as sheafs
import json
import timeit
import param as param

# Configurations
#  move this to config file
#######################################################################################################################
zugfolge =  param.zugfolge
epsilon = param.epsilon
T =  param.T
custom_time = param.custom_time

# current configuration
all_models = param.all_models

timeout = param.timeout

feasibility_stop = param.feasibility_stop
feasibility_time_limit = param.feasibility_time_limit

path = r'/Users/deniserings/Documents/zib/s-bahn-data/processed/'
#path = r'/data/optimi/optimi/kombadon/drings/SBahn/s-bahn-data/processed/'
#out_path = r'/data/optimi/optimi/kombadon/drings/SBahn/s-bahn-data/scripts/DeniseMA/processed/'
out_path = r'/Users/deniserings/Documents/zib/s-bahn-data/scripts/DeniseMA/processed/'

results_file = out_path + 'results_lp_relaxation_2803.csv'

#######################################################################################################################

# all_models =   ['BBER_BBU','BBKS_BWT','BBOS_BWIN_BTG', 'BGAS_BKW', 'BNB_BSNH_BSAL_BPHD', 'BBUP_O','BBUP_W',
#              'BPKW_BKRW_BSNF_O', 'BWKS_medium_september','BGB_BWES']
#

semicolon = ['BBER_BBU','BBUP_O','BBUP_W',
              'BPKW_BKRW_BSNF_O', 'BWKS_medium_september']
# current configuration

comment = ''
versions = [(('h', 'continuous'),('b', 'continuous'))]

y_bars ={}
y_dict = {}
for ((h_var, type_h),(b_var, type_b)) in versions:

    for modelname in all_models:
        print(modelname)
        model_path = path + 'Denise_instances/' + modelname +'/'
        model_out_path = out_path + modelname + '/original/LP_based/'

        if modelname in semicolon:
            sep = ';'
        else:
            sep = ','

        # read input
        ean, ean_noH, curly_H, sheaf_dict, alternatives_dict = ri.read_input(model_path, modelname, T, epsilon, zugfolge, sep)

        # clean log files
        filename = model_out_path+ modelname +'_lp'


        try:
            os.remove(filename + '.log')
        except OSError:
            pass

        start = timeit.default_timer()
        model,p,pi,y,y_bar,h,b = LP.LP_relaxation(modelname, ean, alternatives_dict, 200,
                                               epsilon, zugfolge, curly_H,sheaf_dict,
                                               filename,
                                               h_type=type_h, b_type=type_b,
                                               timeout=timeout, no_improvement_stop = True,
                                                inequality = True)

        stop = timeit.default_timer()
        lp_relaxation_time = stop - start

        try:
            table, time_out, objective,bound,gap,sol_time,solution_count, solve_interrupted = log.evaluate_log(filename + '.log')
            log_dict = log.create_log_dict(table, detailed=True)
            log_dict['Incumbent'] = util.no_solution_substitute(log_dict['Incumbent'], -100)
            first_sol_index, first_sol_time, first_sol_obj, first_sol_gap = util.get_first_sol(log_dict)
            custom_time_cutoff_index, custom_time_obj, custom_time_gap = util.get_sol_custom_time_cutoff(log_dict,
                                                                                                         custom_time)

            plat_index, plat_time, plat_obj, plat_gap = util.get_first_occ_of_plateau_sol(log_dict,
                                                                                          log_dict['Incumbent'][-1])

            x = {}
            for (i, j) in p:
                x[(i, j)] = (pi[j].X - pi[i].X) + T * p[(i, j)].X

            h_dict = {}
            for e in h:
                h_dict[e] =  h[e].X

            pi_dict = {}
            for v in pi:
                pi_dict[v] = pi[v].X


            # measure integrality of the solution

            integral_count_h, fractional_count_h, new_integral_h = LP.integer_measures(h)
            integral_count_b, fractional_count_b, new_integral_b = LP.integer_measures(b)

            sol_file = filename + '.sol'
            sol, objective = read_solution_file(sol_file)

            # y_bar_nonzero = len(
            #     [(i, j) for (i, j) in sol['y_bar'] if (((i, j) not in alternatives_dict[0]['path']) and
            #                                            (round(sol['y_bar'][(i, j)], 2) != 0))])
            # y_bars[modelname] = y_bar_nonzero
            #
            # y_nonzero = len(
            #     [(i, j) for (i, j) in sol['y'] if (((i, j) not in alternatives_dict[0]['path']) and
            #                                            (round(sol['y'][(i, j)], 2) != 0))])
            # y_dict[modelname] = y_nonzero
            #feasibility_check = check_feasibility(modelname, ean, alternatives_dict, epsilon, zugfolge, curly_H,
            #                        sheaf_dict, model_out_path, sol)
            feasibility_check = 'no check'

            configuration_dict = {'start type': None, 'feasibility_stop': feasibility_stop,
                                  'feasibility_time_limit': feasibility_time_limit,
                                  'overall timeout': timeout, 'sheaf sortierung': None, 'period': T, 'epsilon': epsilon,
                                  'zugfolge': zugfolge, 'penalty': None,
                                  'henkelvorsortierung': False,
                                  'h_type': type_h,
                                  'b_type': type_b,
                                  'comment': comment,
                                  'feasibility checked': feasibility_check}

            json.dump(configuration_dict, open(filename+'_configurations.txt', 'w'))

            row = [modelname, comment,type_b,type_h, lp_relaxation_time, gap, objective,integral_count_h, new_integral_h,
                   integral_count_b, new_integral_b, feasibility_check ,plat_time, plat_obj, plat_gap]
            header = ['Model', 'comment', 'b type','h type','LP relaxation time', 'gap', 'objective', 'integral_count_h', 'integrality h',
                   'integral_count_b', 'integrality b' , 'feasibility check','plateau_time', 'plateau_time_obj', 'plateau_time_gap']
            log.write_detailed_results_excel(results_file, header, row, create_new_file=False)



        except:
           print("something didn't work", modelname)


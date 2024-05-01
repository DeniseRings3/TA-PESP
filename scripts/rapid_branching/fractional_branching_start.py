import math

from gurobipy.gurobipy import GRB

# import scripts.DeniseMA.scripts.successive_sheafs.successive_sheafs_functions as ssf
# import scripts.DeniseMA.scripts.successive_stations.successive_stations as station
# import scripts.DeniseMA.scripts.successive_sheafs.sort_alternatives as sort_alt
# import scripts.DeniseMA.scripts.build_ean.read_ean_functions as rd
# import scripts.DeniseMA.scripts.visualisations.visualise_sheafs as vis_sheaf
# import scripts.DeniseMA.scripts.visualisations.visualisations as vis
# #import scripts.build_ean.read_ean_functions as rd
# import networkx as nx
# from collections import defaultdict
#import scripts.DeniseMA.scripts.analyse_results.evaluate_solutions_functions as ev
import analyse_results.evaluate_solutions_functions as ev
#import scripts.DeniseMA.scripts.analyse_results.analyse_log as log
import utils.analyse_log as log
import model.BuildModel as bd
#import csv
#import scripts.DeniseMA.scripts.LPbased.sort_alternatives_improvement as sort
import LPbased.sort_alternatives_improvement as sort
#from bigtree import Node, find_children, tree_to_dict, tree_to_nested_dict, inorder_iter, levelorder_iter, DAGNode
# from datetime import date
# import scripts.DeniseMA.scripts.regelfahrplan.regelfahrplan as regel
# import timeit
#import scripts.DeniseMA.scripts.build_ean.read_entire_input as ri
import build_ean.read_entire_input as ri
# import scripts.DeniseMA.scripts.LPbased.LPmodel as lp
# import scripts.DeniseMA.scripts.model.BuildModel as bd
# import scripts.DeniseMA.scripts.utils.write_timetable as util
import rapid_branching.model as bra
import timeit
# Configurations
#import scripts.DeniseMA.scripts.param as param
import param as param
import os
import datetime
import utils.auswertung as util
#import param as param


# Configurations
path =  param.path
out_path = param.out_path
zugfolge =  param.zugfolge
epsilon = param.epsilon
T =  param.T


# current configuration
all_models = param.all_models
#all_models = ['BBUP_W']
timeout = param.timeout
feasibility_stop = param.feasibility_stop
feasibility_time_limit = param.feasibility_time_limit
results_file = out_path + param.results_file
custom_time = param.custom_time

path = r'/Users/deniserings/Documents/zib/s-bahn-data/processed/'
#path = r'/data/optimi/optimi/kombadon/drings/SBahn/s-bahn-data/processed/'
#out_path = r'/data/optimi/optimi/kombadon/drings/SBahn/s-bahn-data/scripts/DeniseMA/processed/'
out_path = r'/Users/deniserings/Documents/zib/s-bahn-data/scripts/DeniseMA/processed/'



comment = 'Branching start sol'
timestamp =  datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
timestamp_file = datetime.datetime.now().strftime("%Y%m%d%H%M")
print(timestamp_file)

script_directory = os.path.dirname(os.path.realpath(__file__))
print(script_directory)

# all_models = ['BBKS_BWT','BBOS_BWIN_BTG', 'BGAS_BKW', 'BNB_BSNH_BSAL_BPHD', 'BBUP_O','BBUP_W',
#             'BPKW_BKRW_BSNF_O', 'BWKS_medium_september']
# #,'BGB_BWES',
#
semicolon = ['BBER_BBU','BBUP_O','BBUP_W','BPKW_BKRW_BSNF_O', 'BWKS_medium_september']
mip_start_sol_dict = {}
lp_opt_sol_dict = {}

overall_timeout = 30*60

for modelname in all_models:
    filename = out_path  + modelname +'/RENS/' + modelname + '_subMBP.sol'
    sol_new, mip_objective = ev.read_solution_file(filename)
    mip_start_sol_dict[modelname] = sol_new


    filename = out_path + modelname + '/original/LP_based/'+ modelname + '_b_continuous_h_continuous.sol'
    sol_new, objective = ev.read_solution_file(filename)
    lp_opt_sol_dict[modelname] = sol_new



for modelname in all_models:

    print(modelname)
    model_path = path + 'Denise_instances/' + modelname +'/'
    model_out_path = out_path + modelname + '/Branching/'

    #print(mip_start_sol_dict[modelname]['b'])
    #print(lp_opt_sol_dict[modelname]['b'])

    if modelname in semicolon:
        sep = ';'
    else:
        sep = ','

    # read input
    ean, ean_noH, curly_H, sheaf_dict, alternatives_dict = ri.read_input(model_path, modelname, T, epsilon, zugfolge, sep)

    for F in alternatives_dict:
        if F not in mip_start_sol_dict[modelname]['b']:
            mip_start_sol_dict[modelname]['b'][F] = 0

    #print(len(mip_start_sol_dict[modelname]['b']))
    #print(len(lp_opt_sol_dict[modelname]['b']))
    # clean log files
    filename = model_out_path+ modelname
    param.write_config(filename)
    try:
        os.remove(filename + '.log')
    except OSError:
        pass

    # # ratio of fixed integral variables
    #
    # rins_epsilon = 0.0005# keine ahnung was da sinn macht
    # mfr = 0.5

    activated_set = []
    B_star = [] # fixed_to_1_set
    for F in alternatives_dict.keys():
        print(lp_opt_sol_dict[modelname]['b'][F])

        if lp_opt_sol_dict[modelname]['b'][F] > 0.5:
            lp_opt_sol_dict[modelname]['b'][F] = 1

            activated_set.append(F)
        else:
            lp_opt_sol_dict[modelname]['b'][F] = 0


    # sortiere B_star irgendwie clever
    ratio = 1
    sortierungen = []

    integer_values = [F for F in lp_opt_sol_dict[modelname]['b'] if lp_opt_sol_dict[modelname]['b'][F] == 1]

    # 1: random
    fixed_subset = sort.random_selection(integer_values, ratio, alternatives_dict, sheaf_dict)
    sortierungen.append(('random', ratio, fixed_subset))

    # sort by anzahl ausgeschlossener alternativen
    B_star = sort.sorted_by_excluded_alternatives(activated_set, ratio, alternatives_dict,
                                                            sheaf_dict)
    sortierungen.append(('other alternatives',ratio, B_star))

    # # sort by anzahl kanten
    # B_star = sort.sorted_by_edges(equality_set, ratio, alternatives_dict, sheaf_dict)
    # sortierungen.append(('edges in F', B_star))
    #
    # # 3
    # # sort by activated headways
    # B_star = sort.sorted_by_headways(equality_set, ratio, alternatives_dict, sheaf_dict,curly_H)
    # sortierungen.append(('headways', B_star))
    # #
    # # # sort by fractionality
    # # B_star = sort.sort_by_fractionality(ean_noH, equality_set, alternatives_dict, lp_opt_sol_dict[modelname])
    # # sortierungen.append(('fractionality', B_star))
    # #

    # custom sort henkelanbindungen und abstellgleiswenden fixieren
    # Achtung!!! hier MIP lösung
    # alternatives_list = [F for F in mip_start_sol_dict[modelname]['b'] if mip_start_sol_dict[modelname]['b'][F] == 1]
    # B_star = sort.custom_sort(alternatives_dict, alternatives_list)
    # sortierungen.append(('custom', B_star))

    # sort by slack

    fixed_subset = sort.sort_by_slack(alternatives_dict, lp_opt_sol_dict[modelname], ratio, ean, activated_set)
    sortierungen.append(('slack', ratio, fixed_subset))
    print('slack', fixed_subset)

    for type,ratio,sortierung in sortierungen:
        print(type, sortierung)


    for (type,ratio,B_star) in sortierungen:
        running_time = 0
        print(type,B_star)
        #filename = model_out_path + modelname + '_'+str(type)+'_subMBP'
        filename = model_out_path + modelname + '_'+str(type)+'_subMBP' + timestamp_file

        # smaller B sets
        B_sets = []
        B = B_star
        while len(B) > 1:
            B_sets.append(B)
            half = math.ceil(len(B) / 2)
            B = B[0:half]

        if len(B_sets) <= 1:
            running_time = 0
            break

        print('B sets',B_sets)
        sol_found = False
        #B_sets.remove(B_sets[0])
        level = 0
        while (running_time <= overall_timeout) and (sol_found == False) and (level != len(B_sets)-1):
            start = timeit.default_timer()

            for level,equality_set in enumerate(B_sets):
                print('equality set',equality_set)
                comment = str(equality_set)
                equality_ratio = 1 #

                rins_epsilon = 0
                m,p,pi,y,y_bar,h,b = bra.branching_MIP(modelname, ean, alternatives_dict, T, epsilon, zugfolge, curly_H,
                                                 sheaf_dict,
                                               lp_opt_sol_dict[modelname],mip_start_sol_dict[modelname], equality_set, rins_epsilon,
                                               model_out_path, timeout= 10, sol = lp_opt_sol_dict[modelname],
                                                filename=filename, relaxed = True, feasibility_stop = True, feasibility_time_limit = 2)

                print('solution count',m.SolCount)
                stop = timeit.default_timer()
                running_time += stop - start

                if m.SolCount >= 1:
                    print('found a solution')
                    sol_found = True
                    break
                    obj = m.getObjective()
                    curr_objective = obj.getValue()
                #     if curr_objective < mip_objective:
                #         print('progress')
                #         break
                # else:
                #     continue

        if m.status == GRB.INFEASIBLE or m.SolCount < 1:
            solvable = False
            gap = '-'
            objective = '-'
            time = '-'
            feasibility_check = False
            time_out = False
            first_sol_time = -1
            first_sol_obj = -1
            first_sol_gap = -1
            # custom_time = -1
            custom_time_obj = -1
            custom_time_gap = -1
        else:
            solvable = True
            sol_file = filename + '.sol'
            sol, objective = ev.read_solution_file(sol_file)

            table, time_out, objective, bound, gap, time, solution_count, solve_interrupted = log.evaluate_log(
                filename + '.log')
            m, p, pi, y, y_bar, h, b = bd.set_up_model(modelname, ean, alternatives_dict, 200, epsilon, zugfolge,
                                                       curly_H,
                                                       sheaf_dict, model_out_path,
                                                       timeout= 2,
                                                       feasibility_stop=True,
                                                       feasibility_time_limit=2, sol=sol, test_start=True,
                                                       filename=filename + '_test')

            # table, time_out, original_objective, bound, original_gap, time_original, solution_count, solve_interrupted = log.evaluate_log(
            #     filename + '_test' + '.log')

            log_dict = log.create_log_dict(table, detailed=True)
            log_dict['Incumbent'] = util.no_solution_substitute(log_dict['Incumbent'], -100)
            first_sol_index, first_sol_time, first_sol_obj, first_sol_gap = util.get_first_sol(log_dict)
            custom_time_cutoff_index, custom_time_obj, custom_time_gap = util.get_sol_custom_time_cutoff(log_dict,
                                                                                                         custom_time)



            if m.status == GRB.INFEASIBLE or m.SolCount < 1:
                print('not a solution')
                feasibility_check = False
            else:
                print('found a feasible solution')
                feasibility_check = True

        header = ['Model', 'comment', 'filename', 'date', 'time', 'timeout', 'gap in %', 'objective',
                  'solvable', 'type', 'level', 'feasibility check', 'prev time',
                  'first_sol_time', 'first_sol_obj', 'first_sol_gap',
                  'custom_time', 'custom_time_obj', 'custom_time_gap'
                  ]

        filename_short = modelname + '_subMBP_' + timestamp_file
        row = [modelname, comment, filename, timestamp, time, time_out, gap, objective,
               solvable, type, str(level) + '/' + str(len(B_sets)), feasibility_check,'-',
               first_sol_time, first_sol_obj, first_sol_gap,
               custom_time, custom_time_obj, custom_time_gap]


        log.write_detailed_results_excel(results_file, header, row, create_new_file=False)
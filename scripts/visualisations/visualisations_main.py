# import pandas as pd
# import numpy as np
from collections import defaultdict, Counter
# import csv
# import networkx as nx
# import openpyxl
# import os
# from collections import Counter
# from ast import literal_eval
# import BuildModel as bd
# import read_ean_functions as rd
# import heuristics as heu
import matplotlib.pyplot as plt
#from visualisations import *
# #from scripts.timetabling.EANFunctions import *
import read_ean_functions as rd
import math

import scripts.DeniseMA.scripts.visualisations.visualisations as vis

x_lower = -100
x_upper = 100
y_lower = -100
y_upper = 100
def visualize_line_graph_all_sheafs(ean,modelname, h = {}, timetable = {}, Filename = "", curr_line = -1, sheaf_list = []):
    # split ean in separate eans for the lines
    line_eans_dict = vis.get_line_eans(ean)
    lines = list(line_eans_dict.keys())


    if curr_line != -1:
        lines = [curr_line]

    for line in lines:

        #print('line',line)
        line_ean = line_eans_dict[line]
        end_nodes = vis.get_ends_of_line(line_ean)
        bst_to_event_dict = vis.get_bst_to_event_dict(line_ean)
        #print('bst to event', bst_to_event_dict)
        bst_dict = vis.create_bst_to_gleis_dict(line_ean.nodes)
        #print('bst zu beginn', bst_dict)
        #print('all bst on line', list(bst_to_event_dict.keys()))
        #print(end_nodes)
        #print(bst_to_event_dict)
        bst_graph = vis.get_line_sequence(line_ean)


        end_nodes = vis.get_end_nodes(bst_graph)
        core_line = vis.get_core_line(bst_graph, end_nodes)
        #print('core line', core_line)
        upper_lower_dict = vis.upper_lower_line(line_ean, bst_graph, core_line)
        #print('upper lower dict')
        #print(upper_lower_dict)
        y_dist_track_track, y_dist_left_right, x_dist_arr_dep, x_dist_bst_to_pocket = vis.compute_distances(x_lower,
                                                                                                        x_upper,
                                                                                                        y_lower,
                                                                                                        y_upper,
                                                                                                        upper_lower_dict)

        #         #
        bst_data, line_seq = vis.get_bst_data(core_line, bst_graph, y_lower, y_upper, y_dist_track_track)
        print('bst data')
        print(bst_data)
        count = defaultdict(lambda: 0)
        for bst in list(bst_data.keys()):
            count[bst] = 1
        platform_positions, count = vis.platformpositions_by_bst(bst_data, line_seq, upper_lower_dict, bst_dict, count,
                                                             y_dist_track_track, x_dist_bst_to_pocket)
        #print('platform position')
        # for p in platform_positions:
        #     print(p)
        #     print(platform_positions[p])

        gleis_dict = vis.create_gleis_to_event_dict_line(line_ean, line, False)
        print([v for v in line_ean.nodes() if 'henkel' in v])
        print('line', line)
        print('gleis dict', gleis_dict)

        positions, label_positions = vis.positions_by_coarse(platform_positions, gleis_dict, line_ean,
                                                        y_dist_left_right, x_dist_arr_dep)

        #print(line)
        n  = 5 # sheafs per pic
        chunks = [sheaf_list[i * n:(i + 1) * n] for i in range((len(sheaf_list) + n - 1) // n)]

        if len(chunks[-1]) == 1 and len(chunks)>=2:
            chunks[-2].extend(chunks[-1])
            chunks.remove(chunks[-1])
        print('chunks',chunks)

        for chunk_count,sheaf_chunk in enumerate(chunks):
            figure, axis = plt.subplots(len(sheaf_chunk), 1)
            figure.suptitle(line)
            for index,sheafs in enumerate(sheaf_chunk):
                if Filename != "":
                    if curr_line != -1:
                        newfilename = Filename + modelname + '_'+'curr_'+str(line)+'_' + str(chunk_count) + '_vis.png'
                    else:
                        newfilename = Filename + modelname +'_'+ str(line) + '_vis.png'
                else:
                    newfilename=""

                if h != {}:
                    sol = h[line][tuple(sheafs)]
                else:
                    sol = []

                #print('index',index)
                vis.draw_graph(line_ean, bst_dict, y_dist_track_track, x_dist_bst_to_pocket, x_dist_arr_dep, pos=positions,
                           label_pos=label_positions, simple_labels=False, sol = sol, timetable = timetable,
                           filename = newfilename,
                               ax= axis[index])
                           #fig = figure[math.floor(index/2)][index % 2] )
            plt.subplots_adjust(wspace=0, hspace=0)
            plt.savefig(newfilename, dpi=100, bbox_inches="tight")
            plt.close()
            #plt.show()


    return

def visualize_line_graph(ean,modelname, h = {}, timetable = {}, Filename = "", curr_line = -1):
    # split ean in separate eans for the lines
    line_eans_dict = vis.get_line_eans(ean)
    lines = len(list(line_eans_dict.keys()))
    figure, axis = plt.subplots(math.ceil(lines/2), 2)
    for index,line in enumerate(line_eans_dict.keys()):
        #print('line',line)
        line_ean = line_eans_dict[line]
        end_nodes = vis.get_ends_of_line(line_ean)
        bst_to_event_dict = vis.get_bst_to_event_dict(line_ean)
        #print('bst to event', bst_to_event_dict)
        bst_dict = vis.create_bst_to_gleis_dict(line_ean.nodes)
        #print('bst zu beginn', bst_dict)
        #print('all bst on line', list(bst_to_event_dict.keys()))
        #print(end_nodes)
        #print(bst_to_event_dict)
        bst_graph = vis.get_line_sequence(line_ean)


        end_nodes = vis.get_end_nodes(bst_graph)
        core_line = vis.get_core_line(bst_graph, end_nodes)
        #print('core line', core_line)
        upper_lower_dict = vis.upper_lower_line(line_ean, bst_graph, core_line)
        #print('upper lower dict')
        #print(upper_lower_dict)
        y_dist_track_track, y_dist_left_right, x_dist_arr_dep, x_dist_bst_to_pocket = vis.compute_distances(x_lower,
                                                                                                        x_upper,
                                                                                                        y_lower,
                                                                                                        y_upper,
                                                                                                        upper_lower_dict)

        #         #
        bst_data, line_seq = vis.get_bst_data(core_line, bst_graph, y_lower, y_upper, y_dist_track_track)
        #print('bst data')
        #print(bst_data)
        count = defaultdict(lambda: 0)
        for bst in list(bst_data.keys()):
            count[bst] = 1
        platform_positions, count = vis.platformpositions_by_bst(bst_data, line_seq, upper_lower_dict, bst_dict, count,
                                                             y_dist_track_track, x_dist_bst_to_pocket)
        #print('platform position')
        # for p in platform_positions:
        #     print(p)
        #     print(platform_positions[p])

        gleis_dict = vis.create_gleis_to_event_dict_line(line_ean, line, False)
        #print('gleis dict', gleis_dict)

        positions, label_positions = vis.positions_by_coarse(platform_positions, gleis_dict, line_ean,
                                                        y_dist_left_right, x_dist_arr_dep)

        #print(line)
        print('line', line)
        print('positions',positions)
        if Filename != "":
            if curr_line != -1:
                newfilename = Filename + modelname + '_'+'curr_'+str(curr_line)+'_' + str(line) + '_vis.png'
            else:
                newfilename = Filename + modelname +'_'+ str(line) + '_vis.png'
        else:
            newfilename=""
        if h != {}:
            sol = h[line]
        else:
            sol = []

        print('index',index)
        axis[math.floor(index/2)][index % 2] = vis.draw_graph(line_ean, bst_dict, y_dist_track_track, x_dist_bst_to_pocket, x_dist_arr_dep, pos=positions,
                   label_pos=label_positions, simple_labels=False, sol = sol, timetable = timetable,
                   filename = newfilename,
                       ax= axis[math.floor(index/2)][index % 2])
                       #fig = figure[math.floor(index/2)][index % 2] )
    plt.subplots_adjust(wspace=0, hspace=0)
    plt.show()


    return






x_lower = -100
x_upper = 100
y_lower = -100
y_upper = 100

#path = r'/Users/deniserings/Documents/zib/s-bahn-data/processed/'
path = r'/data/optimi/optimi/kombadon/drings/SBahn/s-bahn-data/processed/'

all_models = ['BNB_BSNH_BSAL_BPHD'] #['BBER_BBU','BBKS_BWT','BBOS_BWIN_BTG', 'BGAS_BKW','BGB_BWES','BNB_BSNH_BSAL_BPHD']

#out_path = r'/Users/deniserings/Documents/zib/s-bahn-data/scripts/DeniseMA/'
out_path = r'/data/optimi/optimi/kombadon/drings/SBahn/s-bahn-data/scripts/DeniseMA/'

for modelname in all_models:
    print('modelname', modelname)
    model_path = path + modelname + '/generic_tt_input/'

    # read EAN
    ean_file = model_path + modelname + '_ean.csv'
    ean = rd.build_EAN_from_file(ean_file)

    # read alternatives
    alternatives_file = model_path + modelname + '_alternatives.csv'
    alternatives_dict, sheaf_dict, sheaf_to_tuple = rd.read_alternatives(alternatives_file)

    print('modelname: ', modelname)
    visualize_line_graph(ean, Filename = out_path+ '/visualisations/'+modelname +'/')
    #visualize_line_graph(ean)

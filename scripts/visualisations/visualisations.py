import csv
import itertools
from typing import Dict, List, Any
from matplotlib.lines import Line2D
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
import matplotlib.colors as colors
import math
import numpy as np
from collections import defaultdict
import os
from matplotlib.patches import Rectangle

#from scripts.timetabling.EANFunctions import *
#import build_ean.read_ean_functions as rd

directory = os.getcwd()
print('visualisations working directory',directory)
import scripts.DeniseMA.scripts.build_ean.read_ean_functions as rd
#import build_ean.read_ean_functions as rd

def upper_lower_line(ean, bst_graph, core_line):
    ean_driving_arcs = [(i,j) for (i,j) in ean.edges if (ean[i][j]['type'] == 'driving' or
                                                         ean[i][j]['type'] == 'henkel-from' or
                                                         ean[i][j]['type'] == 'henkel-to')  and
                        (ean.nodes[i]['gleistyp'] != 'A' and ean.nodes[j]['gleistyp'] != 'A') ]
    ean_pocket_arcs = [(i,j) for (i,j) in ean.edges if (ean[i][j]['type'] == 'driving'  and
                        (ean.nodes[i]['gleistyp'] == 'A' or ean.nodes[j]['gleistyp'] == 'A')) ]
    ean_pocket_arcs_tracks = []
    for (i,j) in ean_pocket_arcs:
        origin = rd.get_gleisbezeichnung(i)
        destination = rd.get_gleisbezeichnung(j)
        if rd.get_gleistyp(i) != 'A':
            ean_pocket_arcs_tracks.append(origin)
        elif rd.get_gleistyp(j) != 'A':
            ean_pocket_arcs_tracks.append(destination)

    ean_pocket_arcs_tracks = list(set(ean_pocket_arcs_tracks))


    #print('ean pocket arcs', ean_pocket_arcs_tracks)
    upper_lower_dict = defaultdict(lambda:defaultdict(lambda:[]))
    if len(core_line)<=1:
        for i,j in ean_driving_arcs:
            bst_i = rd.get_station(i)
            bst_j = rd.get_station(j)
            upper_lower_dict[bst_i]['hin'].append(ean.nodes[i]['gleisbezeichnung'])
            upper_lower_dict[bst_j]['hin'].append(ean.nodes[j]['gleisbezeichnung'])

            upper_lower_dict[bst_i]['rueck'].append(ean.nodes[i]['gleisbezeichnung'])
            upper_lower_dict[bst_j]['rueck'].append(ean.nodes[j]['gleisbezeichnung'])

    else:
        for count,bst in enumerate(core_line):
            for i,j in ean_driving_arcs:
                    if bst in i and core_line[count-1] in j:
                        #print(lineseq[count - 1])
                        upper_lower_dict[bst]['hin'].append(ean.nodes[i]['gleisbezeichnung'])
                        upper_lower_dict[core_line[count-1]]['hin'].append(ean.nodes[j]['gleisbezeichnung'])
                    elif bst in j and core_line[count-1] in i:
                        upper_lower_dict[bst]['rueck'].append(ean.nodes[j]['gleisbezeichnung'])
                        upper_lower_dict[core_line[count-1]]['rueck'].append(ean.nodes[i]['gleisbezeichnung'])


    for bst in upper_lower_dict:
        upper_lower_dict[bst]['hin'] = list(set(upper_lower_dict[bst]['hin']))
        upper_lower_dict[bst]['rueck'] = list(set(upper_lower_dict[bst]['rueck']))

        # entferne henkel
        for gleis in upper_lower_dict[bst]['hin']:
            if 'henkel' in gleis:
                upper_lower_dict[bst]['hin'].remove(gleis)

        for gleis in upper_lower_dict[bst]['rueck']:
            if 'henkel' in gleis:
                upper_lower_dict[bst]['rueck'].remove(gleis)

            # gleise die in hin und rück richtung verwendet werden
        for gleis in upper_lower_dict[bst]['rueck']:
            if gleis in upper_lower_dict[bst]['hin'] and (set(upper_lower_dict[bst]['hin']) != set(upper_lower_dict[bst]['rueck'])):
                #print(' hin und rueck')
                #print(gleis, upper_lower_dict[bst])
                if len(upper_lower_dict[bst]['hin'] ) >= len(upper_lower_dict[bst]['rueck']):
                    upper_lower_dict[bst]['hin'].remove(gleis)
                else:
                    upper_lower_dict[bst]['rueck'].remove(gleis)


        if set(upper_lower_dict[bst]['hin']) == set(upper_lower_dict[bst]['rueck']):
            upper_lower_dict[bst]['rueck'] = [x for x in upper_lower_dict[bst]['hin']]

            half = int(len(upper_lower_dict[bst]['hin'])/2)
            upper_lower_dict[bst]['hin'] = upper_lower_dict[bst]['hin'][:half]
            upper_lower_dict[bst]['rueck'] = upper_lower_dict[bst]['rueck'][half:]

    # add henkel
    for bst in bst_graph.nodes():
        if 'henkel' in bst:
            upper_lower_dict[bst]['hin'].append(bst)

    # add tracks that are only used for turns

    for track in ean_pocket_arcs_tracks:
        bst = track.split('_')[0]
        if (track not in upper_lower_dict[bst]['hin']) and (track not in upper_lower_dict[bst]['rueck']):
            upper_lower_dict[bst]['hin'].append(track)


    return upper_lower_dict


# def upper_lower_line(ean, lineseq):
#     ean_driving_arcs = [(i,j) for (i,j) in ean.edges if (ean[i][j]['type'] == 'driving' or
#                                                          ean[i][j]['type'] == 'henkel-from' or
#                                                          ean[i][j]['type'] == 'henkel-to')  and
#
#                     (ean.nodes[i]['gleistyp'] != 'A' and ean.nodes[j]['gleistyp'] != 'A') ]
#     upper_lower_dict = defaultdict(lambda:defaultdict(lambda:[]))
#     # print('driving arcs')
#     # for e in ean_driving_arcs:
#     #     print(e)
#     for count,bst in enumerate(lineseq):
#         for i,j in ean_driving_arcs:
#             if count == 0:
#                 continue
#
#             if bst in i and lineseq[count-1] in j:
#                 #print(lineseq[count - 1])
#                 upper_lower_dict[bst]['hin'].append(ean.nodes[i]['gleisbezeichnung'])
#                 upper_lower_dict[lineseq[count-1]]['hin'].append(ean.nodes[j]['gleisbezeichnung'])
#             elif bst in j and lineseq[count-1] in i:
#                 upper_lower_dict[bst]['rueck'].append(ean.nodes[j]['gleisbezeichnung'])
#                 upper_lower_dict[lineseq[count-1]]['rueck'].append(ean.nodes[i]['gleisbezeichnung'])
#
#
#     for bst in upper_lower_dict:
#         upper_lower_dict[bst]['hin'] = list(set(upper_lower_dict[bst]['hin']))
#         upper_lower_dict[bst]['rueck'] = list(set(upper_lower_dict[bst]['rueck']))
#         # if set(upper_lower_dict[bst]['hin']) == set(upper_lower_dict[bst]['rueck']):
#         #     half = int(len(upper_lower_dict[bst]['hin']))
#         #     upper_lower_dict[bst]['hin'] = upper_lower_dict[bst]['hin'][:half]
#         #     upper_lower_dict[bst]['rueck'] = upper_lower_dict[bst]['rueck'][half:]
#
#     return upper_lower_dict




def hin_rueck_gleise(lineseq, bst_arc_to_gleisseq_dict, richtung_dict):
    # Bestimme welche Gleise in Hin- und Rückrichtung verwendet werden um unnötige Kreuzungen beim Zeichnen zu vermeiden
    gleisrichtungs_dict = defaultdict(lambda: defaultdict(lambda: []))

    for i, bst in enumerate(lineseq):
        if i == 0:
            for seq in bst_arc_to_gleisseq_dict[(lineseq[0], lineseq[1])]:
                # Hinrichtung
                if richtung_dict[(seq[0], seq[1])] == 1 and richtung_dict[(seq[-2], seq[-1])] == 1:
                    gleisrichtungs_dict[bst]['hin'].append(seq[0])
                    gleisrichtungs_dict[lineseq[1]]['hin'].append(seq[-1])
                # Rückrichtung
                else:  # gleis_net.get_edge_data(seq[0], seq[1])['Richtung'] == -1 and gleis_net.get_edge_data(seq[-2], seq[-1])['Richtung'] == -1 :
                    gleisrichtungs_dict[bst]['rueck'].append(seq[0])
                    gleisrichtungs_dict[lineseq[1]]['rueck'].append(seq[-1])
        else:
            for seq in bst_arc_to_gleisseq_dict[(lineseq[i - 1], lineseq[i])]:
                # Hinrichtung
                if richtung_dict[(seq[-2], seq[-1])] == 1 and richtung_dict[(seq[0], seq[1])] == 1:
                    gleisrichtungs_dict[bst]['hin'].append(seq[-1])
                    gleisrichtungs_dict[lineseq[i - 1]]['hin'].append(seq[0])
                # Rückrichtung
                else:  # gleis_net.get_edge_data(seq[-2], seq[-1])['Richtung'] == -1 and gleis_net.get_edge_data(seq[0], seq[1])['Richtung'] == -1:
                    gleisrichtungs_dict[bst]['rueck'].append(seq[-1])
                    gleisrichtungs_dict[lineseq[i - 1]]['rueck'].append(seq[0])

    for bst in lineseq:
        # lösche dopplungen
        gleisrichtungs_dict[bst]['hin'] = list(set(gleisrichtungs_dict[bst]['hin']))
        gleisrichtungs_dict[bst]['rueck'] = list(set(gleisrichtungs_dict[bst]['rueck']))

    return gleisrichtungs_dict


def draw_graph(subgraph, bst_dict, y_dist_track_track,  x_dist_bst_to_pocket, x_dist_arr_dep, pos={},
               label_pos={}, simple_labels=True, sol=[], timetable={}, filename='', figsize=(12, 9),box = True,
               ax = None, fig = None, title = '', edge_labels = {}, type_dict = {}):



    # if ax != None:
    #     ax = ax
    #     plt.sca(ax)
    #     plt.title(title)
    # # else:
    # #     #fig.suptitle(title)
    # #     ax = plt.gca()
    # if fig != None:
    #     fig = fig
    # else:
    #     fig = plt.gcf()
    fig = plt.gcf()
    ax = plt.gca()
    fig.set_size_inches(*figsize)  # (12, 9)
    fig.suptitle(title)



    if label_pos == {}:
        label_pos = pos
    color_map = {'driving': 'black', 'waiting': 'g', 'wende': 'r', 'headway': 'cyan', 'turn': 'r',
                 'henkel-to': 'silver', 'henkel-from': 'silver', 'contraction_to': 'magenta', 'contraction_from': 'magenta',
                 'contraction': 'lightblue','inevitable':'hotpink'}

    if type_dict != {}:
        print('type dict')
        edge_colors = [color_map[type_dict[(u,v)]] for u, v in subgraph.edges()]
        print([type_dict[(u,v)] for u, v in subgraph.edges()])
    else:
        edge_colors = [color_map[subgraph[u][v]['type']] for u, v in subgraph.edges()]

    # verschiedene node Farben für die verschiedenen Linien
    colors_list = list(colors._colors_full_map.values())
    nodes_color_map = dict((i, j) for i, j in enumerate(colors_list))
    #nodes_colors = [nodes_color_map[subgraph.nodes[u]['line']] for u in subgraph.nodes()]
    type_colors = {'dep': {'right':'gold','left':'lemonchiffon'},
                   'arr':{'right':'gray', 'left':'lightgray'}, None:{None:'b'}}

    nodes_colors = [type_colors[subgraph.nodes[u]['arr_dep']][subgraph.nodes[u]['direction']] for u in subgraph.nodes()]

    labels_dict = {}
    for node in subgraph.nodes():
        if simple_labels:
            labels_dict[node] = node[:node.rfind("_") + 2] + '-' + subgraph.nodes[node]['typ'] + '-' + \
                                subgraph.nodes[node]['direction']
        elif timetable != {}:
            labels_dict[node] = round(timetable[node],2)
        else:
            labels_dict[node] = node
    #abels_dict = {}
    if pos != {}:
        nx.draw_networkx_labels(subgraph, pos=label_pos, labels=labels_dict, font_size=8)
        nx.draw_networkx(subgraph, pos=pos, node_color=nodes_colors, edge_color=edge_colors, verticalalignment='bottom',
                         connectionstyle="arc3,rad=0.15", alpha=0.5, with_labels=False, ax = ax)
    else:
        nx.draw_networkx(subgraph, node_color=nodes_colors, edge_color=edge_colors, verticalalignment='bottom',
                         connectionstyle="arc3,rad=0.15", labels=labels_dict)
    if sol != []:
        sol_edge_colors = []
        # male die Kanten aus der PESP Lösung dick
        if type_dict != {}:
            print('type dict')
            sol_edge_colors = [color_map[type_dict[(u, v)]] for u, v in sol]
            print([type_dict[(u, v)] for u, v in subgraph.edges()])
        else:
            sol_edge_colors = [color_map[subgraph[u][v]['type']] for u, v in sol]
        # for (u, v) in sol:
        #     sol_edge_colors.append(color_map[subgraph[u][v]['type']])

        nx.draw_networkx_edges(subgraph, pos, edgelist=sol, alpha=1, width=4, edge_color=sol_edge_colors,
                               connectionstyle="arc3,rad=0.15", ax = ax)

    # if timetable != {}:
    #     edge_labels = {}
    #     # for (i, j) in subgraph.edges:
    #     #     # obere und untere schranke der Kante als Label
    #     #     edge_labels[(i, j)] = f"[{subgraph[i][j]['l'] / 10.0:.1f},{subgraph[i][j]['u'] / 10.0:.1f}]"
    #
    #     #nx.draw_networkx_labels(subgraph, pos=pos, labels=timetable, font_size=8)
    #     nx.draw_networkx_edge_labels(subgraph, pos, edge_labels= edge_labels, label_pos = 0.5,  font_size= 8,ax = ax )

    if edge_labels != {}:
        nx.draw_networkx_edge_labels(subgraph, pos, edge_labels=edge_labels, label_pos=0.4, font_size=8, ax=ax)

    if box ==True:
        group_tracks_dict = group_tracks(pos)
        group_bst_dict = group_bst(pos)

        overall_max_y = max([max([t for t in group_bst_dict[bst]['y']]) for bst in group_bst_dict])
        overall_min_y = min([min([t for t in group_bst_dict[bst]['y']]) for bst in group_bst_dict])
        overall_max_x = max([max([t for t in group_bst_dict[bst]['x']]) for bst in group_bst_dict])
        overall_min_x = min([min([t for t in group_bst_dict[bst]['x']]) for bst in group_bst_dict])

        all_rectangles = []
        x_dist_bst_to_bst = 0
        for track in group_tracks_dict:
            if 'henkel' in track:
                continue
            bst = track[:track.find('_')]

            smallest_y, biggest_y, smallest_x, biggest_x = get_closest_node(group_tracks_dict, group_bst_dict, bst_dict, bst)
            min_max_dict = get_min_max_dist(smallest_y, biggest_y, overall_min_y, overall_max_y, y_dist_track_track)
            min_max_dict_x = get_min_max_dist(smallest_x, biggest_x, overall_min_x, overall_max_x, x_dist_bst_to_pocket)

            minimum = min([t for t in group_tracks_dict[track]['y']])
            maximum = max([t for t in group_tracks_dict[track]['y']])
            y_dist = min([abs(min_max_dict[track][0]-minimum),  abs(min_max_dict[track][1]-maximum)])

            minimum = min([t for t in group_tracks_dict[track]['x']])
            maximum = max([t for t in group_tracks_dict[track]['x']])
            x_dist = min([abs(min_max_dict_x[track][0] - minimum), abs(min_max_dict_x[track][1] - maximum)])

            if x_dist == 0:
                x_dist = x_dist_arr_dep
            x_dist_bst_to_bst = max([x_dist_bst_to_bst, x_dist])

            anchor_point, width, height = compute_box_limits(group_tracks_dict[track],x_dist, y_dist) # 1.5*x_dist_bst_to_pocket
            plt.sca(ax)
            plt.gca().add_patch(Rectangle(anchor_point, width, height, linewidth=1, edgecolor='b', facecolor='none'))
            plt.text(anchor_point[0], anchor_point[1], track[track.find('_')+1:], color='b', fontsize=10)




        for bst in group_bst_dict:
            anchor_point, width, height = compute_box_limits(group_bst_dict[bst], 1.25*x_dist_bst_to_bst,
                                                             1.5*y_dist_track_track, bst = [overall_min_y,overall_max_y]) #2*x_dist_bst_to_pocket
            all_rectangles.append((anchor_point, width, height,bst))
            plt.gca().add_patch(Rectangle(anchor_point, width, height, linewidth=1, edgecolor='skyblue', facecolor='none'))
            if 'henkel' in bst:
                bst = 'henkel'
            plt.text(anchor_point[0], anchor_point[1], bst, color = 'skyblue', fontsize = 12)

        if all_rectangles:
            all_rectangles.sort(key=lambda x: x[0][0])

            x_lim_lower = all_rectangles[0][0][0]-10
            x_lim_upper = all_rectangles[-1][0][0] + all_rectangles[-1][1]+ 10
            y_lim_lower = all_rectangles[0][0][1] - 10
            y_lim_upper = all_rectangles[-1][0][1] + all_rectangles[-1][2]+ 10
            ax.set_xlim(x_lim_lower, x_lim_upper)
            ax.set_ylim(y_lim_lower, y_lim_upper)



    legend_elements = [
        Line2D([0], [0], marker='o', color='w', label='drivin', markerfacecolor='g', markersize=15),
        Line2D([0], [0], marker='o', color='w', label='label2', markerfacecolor='r', markersize=15),
    ]

    color_map_legend = {'driving': 'black', 'waiting': 'g',  'turn': 'r',
                 'henkel': 'silver', 'inevitable': 'hotpink'}
    handles = [Line2D([], [], color=color_map_legend[type], label= type, linewidth = 1 )
              for type in color_map_legend]
    handles.append(Line2D([], [], color='black', label= 'mip = lp = 1', linewidth = 3 ))



    #nx.draw_networkx(G, pos=nx.spring_layout(G), edge_color=(0.8, 0.6, 0.3), node_color=color)
    plt.sca(ax)
    #plt.legend(handles=handles, loc='lower left')

    # if ax != None:
    #     #plt.show()
    #     return ax
    # else:
    #     plt.show()
    #     if filename != "":
    #         plt.savefig(filename, dpi=100, bbox_inches="tight")
    #         plt.close()
    #     else:
    #         plt.show()
    if filename != "":
        plt.savefig(filename, dpi=100, bbox_inches="tight")
        plt.close()
    else:
        plt.show()


def compute_box_limits(coordinates, x_distance, y_distance, bst = []):
    min_x = min(coordinates['x'])
    max_x = max(coordinates['x'])

    if bst:
        min_y = bst[0]
        max_y = bst[1]

    else:
        min_y = min(coordinates['y'])
        max_y = max(coordinates['y'])
    # rectangle anker punkt links unten

    height = max_y - min_y + y_distance/2
    width = max_x - min_x + x_distance /2
    anchor_point = (min_x - x_distance/4, min_y - y_distance/4)

    return anchor_point, width, height
def group_tracks(platform_positions):
    group_track_dict = defaultdict(lambda:defaultdict(lambda:[]))
    for node in platform_positions:
        if 'henkel' in node:
            track = node
        else:
            parts = node.split('_')
            track = parts[0] + '_' + parts[1]

        group_track_dict[track]['x'].append(platform_positions[node][0])
        group_track_dict[track]['y'].append(platform_positions[node][1])

    return group_track_dict

def group_bst(platform_positions):
    group_track_dict = defaultdict(lambda:defaultdict(lambda:[]))
    i=0
    for node in platform_positions:
        parts = node.split('_')
        if 'henkel' in parts[0]:
            bst = parts[0] + '_'+ str(i)
            if platform_positions[node][0] in group_track_dict[bst]['x']:
                group_track_dict[bst]['x'].append(platform_positions[node][0])
                group_track_dict[bst]['y'].append(platform_positions[node][1])
            else:
                i += 1
                bst = parts[0] + '_' + str(i)
                group_track_dict[bst]['x'].append(platform_positions[node][0])
                group_track_dict[bst]['y'].append(platform_positions[node][1])


        else:
            bst = parts[0]
            group_track_dict[bst]['x'].append(platform_positions[node][0])
            group_track_dict[bst]['y'].append(platform_positions[node][1])

    delete = []
    for bst in group_track_dict:
        if group_track_dict[bst]['x']:
            continue
        else:
            delete.append(bst)
    for bst in delete:
        group_track_dict.pop(bst)

    return group_track_dict

def get_closest_node(group_track_dict, group_bst_dict, bst_dict,bst):
    #for bst in group_bst_dict:
    smallest_x = []
    biggest_x = []
    smallest_y = []
    biggest_y = []

    alle_gleise = bst_dict[bst]['Bahnsteiggleise']
    alle_gleise.extend(bst_dict[bst]['Abstellgleise'])

    for track in list(set(alle_gleise)):

        typ = track[track.rfind('_')+1:]
        track_short = track[:track.rfind('_')]
        if track_short in group_track_dict:
            smallest_y.append((track, min(group_track_dict[track_short]['y'])))
            biggest_y.append((track, max(group_track_dict[track_short]['y'])))
            smallest_x.append((track, min(group_track_dict[track_short]['x'])))
            biggest_x.append((track, max(group_track_dict[track_short]['x'])))
    smallest_y.sort(key=lambda x: x[1])
    biggest_y.sort(key=lambda x: x[1])

    return smallest_y, biggest_y, smallest_x, biggest_x

def get_min_max_dist(smallest_y_all,biggest_y_all,overall_min_y, overall_max_y,y_dist):
    min_max_dict = {}

    for (track,y) in smallest_y_all:
        typ = track[track.rfind('_') + 1:]
        track_short = track[:track.rfind('_')]
        smallest_y = [(track,val) for (track,val) in smallest_y_all if typ == track[track.rfind('_') + 1:]]
        biggest_y = [(track, val) for (track, val) in biggest_y_all if typ == track[track.rfind('_') + 1:]]

        count = [i for i, (x, y) in enumerate(smallest_y) if x == track][0]

        if count == 0 and count == len(smallest_y)-1:
            min_max_dict[track_short] = (smallest_y[0][1]-y_dist, biggest_y[0][1] +y_dist)#
            #min_max_dict[track_short] = (overall_min_y - y_dist, overall_max_y + y_dist)  #

        elif count == 0:

            min_max_dict[track_short] = (overall_min_y-y_dist,
                                         find_next_track_of_type(smallest_y, track,typ,1))# smallest_y[count+1][1])

        # only one track


        elif count == len(smallest_y)-1:
            min_max_dict[track_short] = (find_next_track_of_type(smallest_y, track,typ,-1), overall_max_y+y_dist)
            #(smallest_y[count-1][1], overall_max_y)

        else:
            min_max_dict[track_short] = (find_next_track_of_type(biggest_y, track,typ,-1),
                                         find_next_track_of_type(smallest_y, track,typ,1))
                #(biggest_y[count-1][1],smallest_y[count+1][1])

    return min_max_dict

def find_next_track_of_type(array, element,typ,dir):
    start = [i for i,(x,y) in enumerate(array) if x  == element ][0]
    if dir == 1:
        for count,(next_track,val) in enumerate(array[start+dir:]):
            if typ == next_track[next_track.rfind('_') + 1:]:

                return val
    if dir == -1:
        for count,(track,val) in enumerate(reversed(array[:start])):
            if typ == track[track.rfind('_') + 1:]:
                return val

def create_subgraph(G, stations):
    vertexset = set()
    for node in G.nodes:
        for station in stations:
            if station + '_' in node:
                vertexset.add(node)

    return nx.subgraph(G, vertexset)

def create_event_nodes_pocket(l,r,gleis,positions, label_positions, platform_positions, y_dist_left_right):
    positions[r] = (platform_positions[gleis][0], platform_positions[gleis][1] - 0.25* y_dist_left_right)
    label_positions[r] = (positions[r][0], positions[r][1])
    positions[l] = (platform_positions[gleis][0], platform_positions[gleis][1] - 0.75* y_dist_left_right)
    label_positions[l] = (positions[l][0], positions[l][1])
    return positions,label_positions

def create_event_nodes_track(left,right,gleis, dir, positions, label_positions, platform_positions,x_dist_arr_dep,y_dist_left_right):
    # rückrichtung: (dep,arr) -> dir = -1
    # hinrichtung: (arr,dep) -> dir = 1
    #split occurences
    all_occ_labels = list(set([rd.get_occ_label(track) for track in right]))
    all_occ_labels.extend(list(set([rd.get_occ_label(track) for track in left])))
    all_occ_labels.sort()
    first_occ_label = all_occ_labels[0]
    occ_to_nodes_dict = {}
    for occ in all_occ_labels:
        occ_to_nodes_dict[occ] = {'right':[track for track in right if rd.get_occ_label(track)==occ],
                                    'left':[track for track in left if rd.get_occ_label(track)==occ]}

    for l in occ_to_nodes_dict[first_occ_label]['left']:
        if 'arr' in l:
            positions[l] = (
                platform_positions[gleis][0] - dir*0.5 * x_dist_arr_dep, platform_positions[gleis][1] -0.75*dir*y_dist_left_right)
            label_positions[l] = (positions[l][0], positions[l][1])#+ 0.1 * y_dist_left_right)
        if 'dep' in l:
            positions[l] = (
                platform_positions[gleis][0] + dir*0.5 * x_dist_arr_dep, platform_positions[gleis][1] - 0.75*dir*y_dist_left_right)
            label_positions[l] = (positions[l][0], positions[l][1])#+ 0.1 * y_dist_left_right)

    for r in occ_to_nodes_dict[first_occ_label]['right']:
        if 'arr' in r:
            positions[r] = (
                platform_positions[gleis][0] - dir* 0.5*x_dist_arr_dep, platform_positions[gleis][1]- 0.25 * dir*y_dist_left_right)
            label_positions[r] = (positions[r][0], positions[r][1])#+ 0.1 * y_dist_left_right)
        if 'dep' in r:
            positions[r] = (
                platform_positions[gleis][0] + dir* 0.5*x_dist_arr_dep, platform_positions[gleis][1] - 0.25 * dir* y_dist_left_right)
            label_positions[r] = (positions[r][0], positions[r][1])# + 0.1 * y_dist_left_right)


    # stationen die auf einer linie mehrfach besucht werden
    if len(all_occ_labels)>1:
        for index,i in enumerate(all_occ_labels):
            if index == 0:
                continue
            for node in occ_to_nodes_dict[i]['right']:
                prev_node, prev_node_other_dir = get_prev_node(node, all_occ_labels, index)
                try:
                    positions[node] = (positions[prev_node][0], positions[prev_node][1] + dir* 0.5*y_dist_left_right)
                    label_positions[node] = (positions[node][0], positions[node][1])
                except:
                    positions[node] = (positions[prev_node_other_dir][0], positions[prev_node_other_dir][1] + dir *0.5* y_dist_left_right)
                    label_positions[node] = (positions[node][0], positions[node][1])

            for node in occ_to_nodes_dict[i]['left']:
                prev_node, prev_node_other_dir = get_prev_node(node, all_occ_labels, index)
                try:
                    positions[node] = (positions[prev_node][0], positions[prev_node][1] + dir *0.5* y_dist_left_right)
                    label_positions[node] = (positions[node][0], positions[node][1])
                except:
                    positions[node] = (
                    positions[prev_node_other_dir][0], positions[prev_node_other_dir][1] + dir *0.5* y_dist_left_right)
                    label_positions[node] = (positions[node][0], positions[node][1])

    return positions,label_positions

def get_prev_node(node, all_occ_labels, index):
    parts = node.split('_')
    prev_node = parts[0]
    for j in range(1, len(parts) - 3):
        prev_node += '_'
        prev_node += parts[j]
    prev_node += '_' + str(all_occ_labels[index - 1])

    for j in range(len(parts) - 2, len(parts)):
        prev_node += '_'
        prev_node += parts[j]

    prev_node_other_dir = prev_node[0: prev_node.rfind('_')]
    if parts[-1] == 'left':
        prev_node_other_dir += '_' + 'right'
    else:
        prev_node_other_dir += '_' + 'left'

    return prev_node, prev_node_other_dir

def positions_by_coarse(platform_positions, gleis_dict, G, y_dist_left_right, x_dist_arr_dep):
    # bestimme die Koordinaten der Events anhand der Koordinaten der Gleise
    count_bst = 10 # len(lineseq)
    y_lower = -100
    y_upper = 100
    y_dist_left_right = (y_upper-y_lower)/count_bst
    positions = {}
    label_positions = {}
    for gleis in gleis_dict:

        if gleis not in platform_positions.keys():
            print('continue')
            continue

        for node in gleis_dict[gleis]:

            left = sorted([v for v in gleis_dict[gleis] if 'left' in v])
            right = sorted([v for v in gleis_dict[gleis] if 'right' in v])
            # print(node)
            # print('left', left)
            # print('right',right)
            # abstellgleis

            if G.nodes[node]['gleistyp'] == 'A':
                if len(left) == 1 and len(right) == 1: # standard abstellgleis mit arr_right, dep_left‚
                    positions, label_positions = create_event_nodes_pocket(left[0],right[0],gleis, positions, label_positions, platform_positions, y_dist_left_right)
                else:
                    positions, label_positions = create_event_nodes_track(left,right,gleis,1, positions, label_positions, platform_positions,
                                         x_dist_arr_dep, y_dist_left_right)


            else:
                if 'henkel' in gleis:
                    positions[gleis] = (
                    platform_positions[gleis][0], platform_positions[gleis][1])
                    label_positions[gleis] = (positions[gleis][0], positions[gleis][1])

                elif platform_positions[gleis][2] == False: #False
                    # in rückrichtung ist dep links von arrival
                    # links knoten über rechts noten
                    positions, label_positions = create_event_nodes_track(left,right,gleis, -1, positions, label_positions, platform_positions,
                                         x_dist_arr_dep, y_dist_left_right)
                # rückrichtung: (dep,arr) -> dir = -1
                else:  # in hinrichtung ist dep rechts von arrival
                    # links knoten unter rechts noten
                    positions, label_positions = create_event_nodes_track(left, right, gleis, 1, positions,
                                                                          label_positions, platform_positions,
                                         x_dist_arr_dep, y_dist_left_right)


    return positions, label_positions

def platformpositions_by_bst(bst_data, lineseq, gleisrichtung_dict, bst_dict, count, y_dist_track_track, x_dist_bst_to_pocket):
    platform_positions = {}

    # Bestimme Koordinaten der Gleise anhand der vorgebenen Koordinaten der Betriebsstellen
    for i, bst in enumerate(lineseq):
        if 'henkel' in bst:
            platform_positions[bst] = (bst_data[bst]['x'], bst_data[bst]['y'], False)  # False

            continue

        v1, v2 = (float(bst_data[lineseq[i]]['x']), -float(bst_data[lineseq[i]]['y']))

        if (i == len(lineseq) - 1) or ('henkel' in bst_data[lineseq[i + 1]]):
            w1, w2 = (float(bst_data[lineseq[i - 1]]['x']), -float(bst_data[lineseq[i - 1]]['y']))
        else:
            w1, w2 = (float(bst_data[lineseq[i + 1]]['x']), -float(bst_data[lineseq[i + 1]]['y']))

        if i != 0 and ('henkel' not in bst_data[lineseq[i - 1]]):
            z1, z2 = (float(bst_data[lineseq[i - 1]]['x']), -float(bst_data[lineseq[i - 1]]['y']))
        else:
            z1, z2 = (float(bst_data[lineseq[i + 1]]['x']), -float(bst_data[lineseq[i + 1]]['y']))

        next_dx, next_dy = (w1 - v1, w2 - v2)
        prev_dx, prev_dy = (v1 - z1, v2 - z2)

        # if (next_dx, next_dy) != (-prev_dx, -prev_dy) and (next_dx, next_dy) != (prev_dx, prev_dy):  # knick
        #     dx, dy = ((prev_dx + next_dx) / 2, (prev_dy + next_dy) / 2)
        # else:
        dx, dy = (w1 - v1, w2 - v2)

        norm = math.sqrt(dx * dx + dy * dy)
        o1, o2 = (dy / norm, -dx / norm)

        if count[bst] != 0:
            count[bst] -= 1

            for counter, p in enumerate(gleisrichtung_dict[bst]['hin']):
                counter += 1
                #platform_positions[p] = (v1 - 0.5 * y_dist_track_track * o1 * counter / 2, v2 - y_dist_track_track * o2 * counter / 2, False) #False
                platform_positions[p] = (v1 - 0.5 * y_dist_track_track * o1 , v2 - y_dist_track_track * o2*counter / 2, False) #False ** counter

            for counter, p in enumerate(gleisrichtung_dict[bst]['rueck']):
                counter += 1
                if p not in platform_positions:
                    # platform_positions[p] = (v1 + 0.5 * y_dist_track_track * o1 * counter / 2, v2 + y_dist_track_track * o2 * counter / 2, True)
                    platform_positions[p] = (v1 + 0.5 * y_dist_track_track * o1 , v2 + y_dist_track_track * o2*counter / 2, True) #True

    # Kehrgleise
    for count,bst in enumerate(lineseq):
        all_x = [platform_positions[p][0] for p in bst_dict[bst]['Bahnsteiggleise'] if
                 p in platform_positions]  # nicht jede linie nutzt alle gleise deshalb die extra if abfrage

        if all_x == []:
            continue

        min_x = min(all_x)
        max_x = max(all_x)

        all_y = [platform_positions[p][1] for p in bst_dict[bst]['Bahnsteiggleise'] if p in platform_positions]
        min_y = min(all_y)
        max_y = max(all_y)
        n = len(bst_dict[bst]['Abstellgleise'])

        # wenn bst anfang von linie Abstellgleise links, sonst rechts
        if count == 0:
            new_x = np.linspace(min_x - 2* x_dist_bst_to_pocket, min_x - 2*x_dist_bst_to_pocket, n)

        else:
            new_x = np.linspace(max_x + 2*x_dist_bst_to_pocket, max_x + 2*x_dist_bst_to_pocket, n)

        new_y = symmetric_around_centre(min_y,max_y,n,y_dist_track_track)
        for i, kehrgleis in enumerate(bst_dict[bst]['Abstellgleise']):
            platform_positions[kehrgleis] = (new_x[i], new_y[i], False)


    return platform_positions, count

def symmetric_around_centre(min_y,max_y,n,y_dist_track_track, centre = []):

    if centre == []:
        centre = min_y + (max_y - min_y)/2
    else:
        centre = centre
    new_y = []
    for i in range(n):
        if i % 2 == 0 and i != 0:
            sign = 1
            fac = (i+1) //2

        elif i == 0:
            sign = 0
            fac=1


        else:
            sign = -1
            fac = (i+1)//2


        new_y.append(centre + sign * fac*y_dist_track_track)

    return new_y

def get_multiplicity_of_bst(all_lines):
    # bestimme wie häufig eine bsts im gesamten Linienplan enthalten ist
    for j, line in enumerate(all_lines):
        # bestimme wie häufig eine bsts innerhalb einer linie enthalten ist
        on_line_dict = defaultdict(lambda: 0)
        for station in line:
            on_line_dict[station] += 1

        for station in line:
            if on_line_dict[
                station] == 1:  # ende der linie ist immer nur einnmal drin, alle anderen mind 2 mal, für hin und rückrichtung
                on_line_dict[station] += 1  # daher zähle hier eins hoch

    return on_line_dict


def get_all_positions(G, all_lines, line_nums, frequences_dict, bst_data, line_bundle, gleis_net, routing_bundle):
    # Main funktion, die zunächst die Koordinaten der Gleise und dann der Eventes bestimmt
    bst_dict = create_bst_to_gleis_dict(G)

    positions = {}
    label_positions = {}

    # Bestimme wie oft die Betriebsstelle insgesamt besucht wird
    count = get_multiplicity_of_bst(all_lines, line_nums, frequences_dict)

    for j, lineseq in enumerate(all_lines):

        line_num = line_nums[j]
        wendeseq = line_bundle.wendeseq[line_num]
        new_lineseq = sort_line(lineseq, wendeseq)

        gleisrichtung_dict = hin_rueck_gleise(new_lineseq, gleis_net, routing_bundle)

        platform_positions, count = platformpositions_by_bst(bst_data, new_lineseq, gleisrichtung_dict, bst_dict, count)

        subgraph_nodes = [node.split("_")[0] for node in platform_positions]
        subgraph = create_subgraph(G, subgraph_nodes)

        for frequ in range(1, int(frequences_dict[line_num]) + 1):
            gleis_dict = create_gleis_to_event_dict_line(subgraph, line_num, frequ, True)
            new_positions, new_label_positions = positions_by_coarse(platform_positions, gleis_dict, G)
            positions.update(new_positions)
            label_positions.update(new_label_positions)

    return positions, label_positions

def create_bst_to_gleis_dict(nodes):
    bst_dict = defaultdict(lambda: defaultdict(lambda: []))

    for node in nodes:
        parts = node.split('_')
        bst = parts[0]
        gleisnummer = parts[1]
        typ = parts[2]
        gleis = bst + '_' + gleisnummer + '_' + typ

        if typ == 'A':
            bst_dict[bst]['Abstellgleise'].append(gleis)

        elif 'henkel' in bst:
            bst_dict[node]['Abstellgleise'] = []
            bst_dict[node]['Bahnsteiggleise'].append(node)

        else: # abzweigungn sollen auch als bahnsteig gelten
            bst_dict[bst]['Bahnsteiggleise'].append(gleis)

    for bst in bst_dict:
        bst_dict[bst]['Bahnsteiggleise'] = list(set(bst_dict[bst]['Bahnsteiggleise']))
        bst_dict[bst]['Abstellgleise'] = list(set(bst_dict[bst]['Abstellgleise']))

    return bst_dict

def create_gleis_to_event_dict_line(G, line, occ=False):
    # gleis to event dict linien scharf
    # wenn occ = True sogar occurence scharf (wird beim Zeichnen in der positions_by_coarse methode verwendet)

    gleis_dict = defaultdict(lambda: [])
    bsts = []
    for node in G.nodes:
        gleis = rd.get_gleisbezeichnung(node)
        if 'henkel' in node:
            print(node)
            print(gleis)
        if G.nodes[node]['line'] == line:
            gleis_dict[gleis].append(node)

    return gleis_dict

# infos_dict = {'station': None,
#                       'gleis': None,
#                       'gleistyp': None,
#                       'line': infos[-3],
#                       'freq_count': infos[-2],
#                       'occ_label': infos[-1],
#                       'arr_dep': None,
#                       'left_right': None,
#                       'henkel': infos[1]} #henkel id


def read_lines(lineconcept, linepool):
    linepool_dict = defaultdict(lambda:defaultdict(lambda:[]))
    # read linepool:
    with open(linepool ) as file_obj:
        reader_obj = csv.reader(file_obj, delimiter =';')
        next(reader_obj)
        # LinienNummer	Klebesequenz	Wendesequenz	Knoten

        for row in reader_obj:
            linenumber = int(row[0])
            klebeseq = row[1]
            wendeseq = row[2]
            node = row[3]

            if linenumber in linepool_dict:
                linepool_dict[linenumber]['Stations'].append(node)
            else:
                linepool_dict[linenumber]['Klebesequenz'] = klebeseq.split(' ')
                linepool_dict[linenumber]['Wendesequenz'] = wendeseq.split(' ')
                linepool_dict[linenumber]['Stations'] = [node]

    # select only those lines in lineconcept
    line_dict = defaultdict(lambda:defaultdict(lambda:[]))
    with open(lineconcept) as file_obj:
        reader_obj = csv.reader(file_obj, delimiter =';')
        next(reader_obj)
        # LineIdx;Freq
        for row in reader_obj:
            linenumber = int(row[0])
            frequ = int(row[1])
            line_dict[linenumber]['Klebesequenz'] = linepool_dict[linenumber]['Klebesequenz']
            line_dict[linenumber]['Wendesequenz'] = linepool_dict[linenumber]['Wendesequenz']
            line_dict[linenumber]['Stations'] = linepool_dict[linenumber]['Stations']
            line_dict[linenumber]['Frequenz'] = frequ

    return line_dict


def sort_line(line_seq, wende_seq):
    # sortiere die Linie so um, dass sie die gleiche Reihenfolge hat wie die Wendesequenz
    if len(wende_seq) > 0:
        new_line = [i for i in line_seq[line_seq.index(wende_seq[0]):]]
        new_line.extend(line_seq[0:line_seq.index(wende_seq[0])])

        return new_line
    else:
        return line_seq


def read_gleis_net(file):

    richtung_dict = {}
    with open(file) as file_obj:
        reader_obj = csv.reader(file_obj, delimiter=';')
        next(reader_obj)
        #Start	Ziel	Strecke	Richtung
        for row in reader_obj:
            richtung_dict[(row[0], row[1])] = row[-1]
    return richtung_dict


def read_bst_arc_to_gleisseq(file):
    # Betriebsstelle von,Betriebsstelle zu, Sequenznummer
    # Anzahl von Links-Abschnitten	Anzahl Nicht-Strecken Abschnitten
    # Anzahl von Gleiswechseln	startet rechts	endet rechts	Knoten
    seq_dict = defaultdict(lambda:defaultdict(lambda: []))
    with open(file) as file_obj:
        reader_obj = csv.reader(file_obj, delimiter=';')
        next(reader_obj)
        # LineIdx;Freq
        for row in reader_obj:
            sequenznum = row[2]
            seq_dict[sequenznum]['bst_tuple'] = (row[0], row[1])
            seq_dict[sequenznum]['path'].append(row[-1])

    bst_arc_to_gleisseq_dict = {}
    for seq in seq_dict:
        bst_tuple = seq_dict[seq]['bst_tuple']
        if bst_tuple in bst_arc_to_gleisseq_dict:
            bst_arc_to_gleisseq_dict[bst_tuple].append(seq_dict[seq]['path'])
        else:
            bst_arc_to_gleisseq_dict[bst_tuple] = [seq_dict[seq]['path']]

    return bst_arc_to_gleisseq_dict


def get_line_eans(ean):
    # unterteile in line eans
    line_eans_dict = {}
    S = [ean.subgraph(c).copy() for c in nx.weakly_connected_components(ean)]
    for s in S:
        u, v = list(s.edges)[0]
        line_num = s.nodes[u]['line']
        # if s.nodes[u]['frequency'] > 1:
        #     #key = str(line_num) +'_'+ str(s.nodes[u]['frequency'])
        #     continue
        line_eans_dict[line_num] = s
    return line_eans_dict

def get_bst_data(core_line, bst_graph, min_y, max_y, y_dist_track_track):
    henkel = [v for v in bst_graph.nodes() if 'henkel' in v]
    adj_to_henkel =  list(set([v  for h in henkel for v in bst_graph.neighbors(h)]))
    # print(adj_to_henkel)
    count_bst = len(core_line) + len(adj_to_henkel)
    x_lower = -100
    x_upper = 100
    distance = min([(x_upper-x_lower)/count_bst,y_dist_track_track])

    bst_data = defaultdict(lambda:defaultdict(lambda:0))
    lineseq = [x for x in core_line]
    for count,station in enumerate(core_line):
        adj_henkel = [h for h in henkel if h in bst_graph.neighbors(station) ]
        #print('adj henkel',adj_henkel)
        if count == 0:
            lineseq.insert(0,adj_henkel)

        else:
            lineseq.insert(len(core_line)+1, adj_henkel)


    for index,bst in enumerate(lineseq):
        if type(bst) is list:
            new_y = symmetric_around_centre(min_y, max_y, len(bst), y_dist_track_track, centre=0)
            for i,henkel in enumerate(bst):
                if index == 0:
                    bst_data[henkel]['x'] = x_lower - 1.25*distance
                else:
                    bst_data[henkel]['x'] = x_lower + 1.25* index* distance
                bst_data[henkel]['y'] = new_y[i]
        else:
            bst_data[bst]['x'] = x_lower + index * distance
            bst_data[bst]['y'] = 0

    lineseq_flattened =  []
    for index,bst in enumerate(lineseq):
        if type(bst) is list:
            for i, henkel in enumerate(bst):
                lineseq_flattened.append(henkel)
        else:
            lineseq_flattened.append(bst)

    #print(lineseq_flattened)

    return bst_data, lineseq_flattened

# def get_bst_data(lineseq):
#     count_bst = len(lineseq)
#     x_lower = -100
#     x_upper = 100
#     distance = (x_upper-x_lower)/count_bst
#     bst_data = defaultdict(lambda:defaultdict(lambda:0))
#     for index,bst in enumerate(lineseq):
#         bst_data[bst]['x'] = x_lower + index*distance
#         bst_data[bst]['y'] = 0
#
#     return bst_data

def compute_distances(x_lower,x_upper,y_lower,y_upper, gleisrichtung_dict):
    x_dist_bst_to_pocket = 20
    x_dist_arr_dep = 0
    y_dist_left_right = 0
    y_dist_track_track = 0

    y_stretch = y_upper - y_lower
    x_stretch = x_upper - x_lower


    max_gleise = max([len(gleisrichtung_dict[bst]['hin']) + len(gleisrichtung_dict[bst]['rueck']) for bst in gleisrichtung_dict])
    y_dist_track_track = min([2*y_stretch / max_gleise,y_stretch/4])

    y_dist_left_right = 0.5* y_dist_track_track


    x_dist_bst_bst = x_stretch / len(list(gleisrichtung_dict.keys()))
    x_dist_arr_dep = 0.4 * x_dist_bst_bst
    x_dist_bst_to_pocket = 0.75 * x_dist_bst_bst


    return y_dist_track_track, y_dist_left_right, x_dist_arr_dep,  x_dist_bst_to_pocket


def get_bst_on_cycle(cycle):
    only_bst = []
    for count,v in enumerate(cycle):
        if count == 0:
            only_bst.append(v)
        elif cycle[count-1] != v:
            only_bst.append(v)
    return only_bst

x_lower = -100
x_upper = 100
y_lower = -100
y_upper = 100
def get_bst_turns(ean):
    bst_turns = []
    for (i, j) in ean.edges():
        if ean.nodes[i]['gleisbezeichnung'] == ean.nodes[j]['gleisbezeichnung']:
            if ((ean.nodes[i]['arr_dep'] == 'arr' and ean.nodes[j]['arr_dep'] == 'dep') and
                (ean.nodes[i]['direction'] == 'right' and ean.nodes[j]['direction'] == 'left')):
                bst_turns.append((i,j))
    bst_turns = list(set(bst_turns))
    return bst_turns

def get_bst_to_event_dict(ean):
    bst_to_event_dict = defaultdict(lambda:[])
    for node in ean.nodes():
        print(node,ean.nodes[node])
        station = ean.nodes[node]['station']
        bst_to_event_dict[station].append(node)
    return bst_to_event_dict


def get_ends_of_line(ean):
    turn_edges = [(i, j) for (i, j) in ean.edges() if ean[i][j]['type'] == 'turn']
    turn_stations = list(set([ean.nodes[i]['station'] for (i, j) in turn_edges]))
    pocket_tracks = list(set([ rd.get_station(node) for node in ean.nodes if ean.nodes[node]['gleistyp'] == 'A']))
    bst_turn_stations = list(set([rd.get_station(i) for (i,j) in get_bst_turns(ean)]))
    henkel = list(set([ node for node in ean.nodes if ean.nodes[node]['gleistyp']== 'henkel']))

    end_nodes = bst_turn_stations
    end_nodes.extend(turn_stations)
    end_nodes.extend(pocket_tracks)
    end_nodes.extend(henkel)
    end_nodes = list(dict.fromkeys(end_nodes))

    return end_nodes

def get_line_sequence(ean):
    bst_graph = nx.DiGraph()
    driving_edges = [(i,j) for (i,j) in ean.edges() if (ean[i][j]['type'] == 'driving' or ean[i][j]['type'] == 'henkel-to'
                                                        or ean[i][j]['type'] == 'henkel-from')]
    driving_edges_bst = list(set([(rd.get_station(i),rd.get_station(j)) for (i,j) in driving_edges]))

    bst_graph.add_edges_from(driving_edges_bst)
    bst_graph.remove_edges_from(nx.selfloop_edges(bst_graph))
    #nx.draw_networkx(bst_graph)
    #plt.show()
    return bst_graph

def get_end_nodes(bst_graph):
    return [v for v in bst_graph.nodes() if (bst_graph.in_degree(v) == 1 and bst_graph.out_degree(v) == 1)]

def get_core_line(bst_graph, end_nodes):
    core_line = bst_graph.copy()
    for v in end_nodes:
        if 'henkel' in v:
            for w in bst_graph.successors(v):
                if 'henkel' not in w:
                    core_line.remove_node(v)
    #nx.draw_networkx(core_line)
    #plt.show()

    if len(core_line) == 1:
        return list(core_line.nodes())
    core_line_ends = [v for v in bst_graph.nodes() if (core_line.in_degree(v) == 1 and core_line.out_degree(v) == 1)]
    if len(core_line_ends) == 0:
        core_line_ends = [v for v in core_line.nodes()]
    print(bst_graph.nodes())
    print('degrees',[(v,core_line.in_degree(v),core_line.out_degree(v)) for v in bst_graph.nodes()])
    #print(core_line_ends)
    if len(core_line_ends) == len(core_line.nodes()):

        start = core_line_ends[0]
        end = [v for v in core_line.predecessors(start)][0]
        all_paths = list(nx.all_simple_paths(core_line, start,end ))
        all_paths = sorted(all_paths, key=len, reverse=True)
        print(sorted(all_paths))
        core_line_sequ = all_paths[0]
        print('core line sequ',core_line_sequ)
    else:
        if len(list(nx.all_simple_paths(core_line, core_line_ends[0], core_line_ends[1]))) == 0:
            core_line_ends = [v for v in bst_graph.nodes() if
                              (core_line.in_degree(v) == 0 and core_line.out_degree(v) == 0)]
            print(core_line_ends)
            #nx.draw_networkx(core_line)
            #plt.show()
            core_line_sequ = list(core_line.nodes())

        else:
            core_line_sequ = list(nx.all_simple_paths(core_line, core_line_ends[0], core_line_ends[1]))[0]
    return core_line_sequ


def draw_station(station,subgraph, arcs_per_station, activated_arcs_per_station, sol,all_arcs = False):
    x_lower = -100
    x_upper = 100

    y_lower = -100
    y_upper = 100

    fig = plt.gcf()
    ax = plt.gca()
    fig.set_size_inches((12,9))  # (12, 9)

    track_coordinates = {}
    dist = (x_upper - x_lower) / len(activated_arcs_per_station[station])
    x_dist_arr_dep = dist/10
    pos_dict = {}

    if all_arcs == True:
        arc_set = arcs_per_station
    else:
        arc_set = activated_arcs_per_station

    for i, track in enumerate(arc_set[station]): #activated_arcs_per_station[station]):
        track_coordinates[track] = x_lower + i * dist

        # sort events by pi val
        begin_activities = [(act_begin,act_end, round(sol['pi'][act_begin],2)) for (act_begin, act_end) in arc_set[station][track]
                            if subgraph[act_begin][act_end]['type'] != 'headway']
        begin_activities = sorted(begin_activities, key=itemgetter(2))
        print(station,track,len(arcs_per_station[station][track]))
        y_dist = (y_upper - y_lower) / len(arcs_per_station[station][track])
        for i,(act_begin,act_end, pi) in enumerate(begin_activities):
            line = rd.get_line(act_begin)
            frequ = rd.get_frequ_count(act_begin)
            if rd.get_direction(act_begin) == 'right' and rd.get_direction(act_end) == 'right':
                pos_dict[act_begin] = (track_coordinates[track] - x_dist_arr_dep,y_upper - i * y_dist )
                pos_dict[act_end] = (track_coordinates[track] + x_dist_arr_dep, y_upper - i * y_dist)
            else:
                pos_dict[act_end] = (track_coordinates[track] - x_dist_arr_dep, y_upper - i * y_dist)
                pos_dict[act_begin] = (track_coordinates[track] + x_dist_arr_dep, y_upper - i * y_dist)

            plt.text(track_coordinates[track]+ x_dist_arr_dep+ dist/8,y_upper - i * y_dist,
                     'line: '+ str(line) +', freq: '+ str(frequ), color='b', fontsize=10)


    color_map = {'driving': 'black', 'waiting': 'g', 'wende': 'r', 'headway': 'cyan', 'turn': 'r',
                 'henkel-to': 'silver', 'henkel-from': 'silver', 'contraction_to': 'magenta', 'contraction_from': 'magenta',
                 'contraction': 'lightblue'}
    edge_colors = [color_map[subgraph[u][v]['type']] for u, v in subgraph.edges()]
    type_colors = {'dep': {'right': 'gold', 'left': 'lemonchiffon'}, 'arr': {'right': 'gray', 'left': 'lightgray'},
                   None: {None: 'b'}}

    nodes_colors = [type_colors[subgraph.nodes[u]['arr_dep']][subgraph.nodes[u]['direction']] for u in subgraph.nodes()]

    #node labels
    labels_dict = {}
    for node in subgraph.nodes:
        labels_dict[node] = round(sol['pi'][node], 2)

    nx.draw_networkx(subgraph, pos=pos_dict, with_labels=True,labels = labels_dict, node_color=nodes_colors, edge_color=edge_colors, verticalalignment='bottom',
                      alpha=0.5) #connectionstyle="arc3,rad=0.15",

    # edge labels
    edge_labels = {}
    for (i, j) in subgraph.edges:
        # obere und untere schranke der Kante als Label
        edge_labels[(i, j)] = f"[{subgraph[i][j]['l'] / 10.0:.1f},{subgraph[i][j]['u'] / 10.0:.1f}]"

    # nx.draw_networkx_labels(subgraph, pos=pos, labels=timetable, font_size=8)
    #nx.draw_networkx_edge_labels(subgraph, pos_dict, edge_labels=edge_labels, label_pos=0.5, font_size=10, verticalalignment='bottom')

    groups_tracks_dict = group_tracks(pos_dict)
    all_rectangles = []
    for track in groups_tracks_dict:
        anchor_point, width, height = vis.compute_box_limits(groups_tracks_dict[track], dist/3,dist/3)  # 1.5*x_dist_bst_to_pocket
        all_rectangles.append((anchor_point, width, height))
        plt.gca().add_patch(Rectangle(anchor_point, width, height, linewidth=1, edgecolor='b', facecolor='none'))
        print('track')
        print(track)
        plt.text(anchor_point[0]+2, anchor_point[1]+2, track[track.find('_') + 1:], color='b', fontsize=10)
        #plt.text(x_lower, y_lower, station, color= 'skyblue', fontsize=32)

        if all_rectangles:
            all_rectangles.sort(key=lambda x: x[0][0])

            x_lim_lower = all_rectangles[0][0][0]
            x_lim_upper = all_rectangles[-1][0][0] + all_rectangles[-1][1]
            y_lim_lower = all_rectangles[0][0][1]
            y_lim_upper = all_rectangles[-1][0][1] + all_rectangles[-1][2]

            plt.text(x_lim_lower+5, y_lim_upper + 2, station, fontsize=20)

            ax.set_xlim(x_lim_lower-10, x_lim_upper+30)
            ax.set_ylim(y_lim_lower-10, y_lim_upper+10)

    # activated edges
    activated_tracks = []
    for track in activated_arcs_per_station[station]:
        activated_arcs_per_station[station][track] = list(set(activated_arcs_per_station[station][track]))
        activated_tracks.extend(activated_arcs_per_station[station][track])

    sol_edge_colors = []
    # male die Kanten aus der PESP Lösung dick
    for (u, v) in activated_tracks:
        sol_edge_colors.append(color_map[subgraph[u][v]['type']])

    nx.draw_networkx_edges(subgraph, pos_dict, edgelist=activated_tracks, alpha=1, width=3, edge_color=sol_edge_colors)
    #nx.draw_networkx(subgraph, pos_dict, node_color=nodes_colors, edge_color=edge_colors, alpha=1, width=4,
    #                           connectionstyle="arc3,rad=0.15") #edge_color=sol_edge_colors,edgelist=sol,
    plt.show()

    return
def draw_solution(ean, activated_arcs_per_station,arcs_per_station,sol = {}, all_arcs = False):

    edges_in_station_dict = defaultdict(lambda:[])
    for (i,j) in ean.edges:
        if (ean[i][j]['type'] == 'driving') or ('henkel' in ean[i][j]['type']):
            continue
        else:
            station = rd.get_station(i)
            edges_in_station_dict[station].append((i,j))

    for station in activated_arcs_per_station:
        activated_tracks = []
        for track in activated_arcs_per_station[station]:
            activated_arcs_per_station[station][track] = list(set(activated_arcs_per_station[station][track]))
            activated_tracks.extend(activated_arcs_per_station[station][track])
            #print(activated_arcs_per_station[station][track])
        print(station)
        if arcs_per_station[station]:
            print(arcs_per_station[station].keys())
            for track in arcs_per_station[station]:
                print(len(arcs_per_station[station][track]))

            if all_arcs:
                subgraph = ean.edge_subgraph(edges_in_station_dict[station]).copy()
                draw_station(station, subgraph, arcs_per_station, activated_arcs_per_station, sol, all_arcs=True)
            else:
                subgraph = ean.edge_subgraph(activated_tracks).copy()
                draw_station(station, subgraph, arcs_per_station, activated_arcs_per_station, sol, all_arcs=False)
        else:
            continue
    return



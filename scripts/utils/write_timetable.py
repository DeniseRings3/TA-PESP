import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict, Counter
#import build_ean.read_ean_functions as rd #
import scripts.DeniseMA.scripts.build_ean.read_ean_functions as rd #
#import visualisations.visualisations as vis #
import scripts.DeniseMA.scripts.visualisations.visualisations as vis #
import pandas as pd

def write_timetable(ean_og,pi,h,x, filename):

    timetable_dict = defaultdict(lambda:[])
    routing_graph = ean_og.edge_subgraph([(i, j) for (i, j) in ean_og.edges() if h[(i, j)] >= 0.5]).copy()
    #nx.draw(routing_graph)
    #plt.show()
    linien_routing_graphs = {}
    start_ziel_dict = {}

    routing_graph_components = [routing_graph.subgraph(c).copy() for c in nx.weakly_connected_components(routing_graph)]

    for s in routing_graph_components:

        line_num = rd.get_line(list(s.nodes)[0])
        linien_routing_graphs[line_num] = s
        # get start and ziel of line
        bst_graph = vis.get_line_sequence(linien_routing_graphs[line_num])
        end_nodes = vis.get_end_nodes(bst_graph)

        core_line = vis.get_core_line(bst_graph, end_nodes)
        print('core line', core_line)
        start_ziel_dict[line_num] = {'start': core_line[0], 'ziel': core_line[-1]}
        start_node = [v for v in s.nodes() if (rd.get_station(v) == start_ziel_dict[line_num]['start']) and rd.get_arr_dep(v) == 'arr' ][0]
        if len(list(nx.simple_cycles(s)))== 0:
            linienverlauf = s.nodes()
            #start_index = linienverlauf.index(start_node)
            #linienverlauf = linienverlauf[start_index:]

            # nx.draw_networkx(s)
            # plt.show()
        # sort nodes on circle according to linienverlauf
        else:
            linienverlauf = list(nx.simple_cycles(s))[0]
        # start_index = linienverlauf.index(start_node)
        # linienverlauf = linienverlauf[start_index:]
        # linienverlauf.extend(linienverlauf[:start_index])


        for v in linienverlauf:
            timetable_dict['Linie'].append(rd.get_line(v))
            timetable_dict['Start'].append(start_ziel_dict[line_num]['start'])
            timetable_dict['Ziel'].append(start_ziel_dict[line_num]['ziel'])
            timetable_dict['Betriebsstelle'].append(rd.get_station(v))
            if 'henkel' in v:
                timetable_dict['Ankunft'].append(1)
                (u, v) = [(u, v) for (u, v) in routing_graph.in_edges(v) if ean_og[u][v]['type'] == 'henkel-to'][0]
                # (v, u) = [(v, u) for (v, u) in ean.out_edges(v) if ean[v][u]['type'] == 'henkel-from'][0]
                print(u,v)
                timetable_dict['Fahrzeit'].append(x[(u, v)])
                timetable_dict['Haltezeit'].append(0)
                timetable_dict['Gleis'].append(rd.get_gleisbezeichnung(v))
                timetable_dict['Minute'].append(pi[v])
                timetable_dict['Typ'].append(ean_og[u][v]['type'])

            else:

                if rd.get_arr_dep(v) == 'arr':
                    timetable_dict['Ankunft'].append(1)
                    if routing_graph.in_edges(v):
                        (u, v) = [(u, v) for (u, v) in routing_graph.in_edges(v) if (ean_og[u][v]['type'] == 'driving') or
                                  (ean_og[u][v]['type'] == 'henkel-to') or (ean_og[u][v]['type'] == 'henkel-from')][0]
                        timetable_dict['Fahrzeit'].append(x[(u, v)])

                    else:
                        timetable_dict['Fahrzeit'].append(None)
                        #print('hier', u,v, x[(u, v)])

                    timetable_dict['Haltezeit'].append(None)
                else:
                    timetable_dict['Ankunft'].append(0)
                    timetable_dict['Fahrzeit'].append(None)

                    (u, v) = [(u, v) for (u, v) in routing_graph.in_edges(v) if ean_og[u][v]['type'] == 'waiting' or
                              ean_og[u][v]['type'] == 'turn'][0]
                    timetable_dict['Haltezeit'].append(x[(u, v)])

                timetable_dict['Gleis'].append(rd.get_gleisbezeichnung(v))
                timetable_dict['Minute'].append(pi[v])
                try:
                    timetable_dict['Typ'].append(ean_og[u][v]['type'])
                except:
                    timetable_dict['Typ'].append(None)


    for key in timetable_dict:
        if key == 7:
            print(key)
            print(timetable_dict[key])
    timetable_df = pd.DataFrame(data=timetable_dict, columns = ['Linie','Start','Ziel','Betriebsstelle',
                                                                 'Ankunft', 'Gleis','Fahrzeit','Haltezeit','Minute', 'Typ'])
    print(timetable_df)
    timetable_df.to_csv(filename+'_timetable.csv', index = False)
    return timetable_df

    # timetable_ean = ean.copy()

    #
    # # füge zum schreiben der tabelle neue knoten für die henkel hinzu
    # henkel_nodes = [v for v in ean.nodes if 'henkel' in v]
    #
    # henkel_to =  [(u,v) for (u,v) in ean.edges if ean[u][v]['type'] == 'henkel-to']
    # henkel_from =  [(v,u) for (v,u) in ean.edges if ean[v][u]['type'] == 'henkel-from']
    #
    # print(henkel_from)

    # new_nodes = [v + 'in' for v in henkel_nodes]
    # new_nodes.append([v + 'in' for v in henkel_nodes])

    # for u,v in henkel_to:
    #
    #     timetable_ean.add_edge(u, v + '_in')
    #     timetable_ean.add_edge(v + '_in', v +'_out')
    #     timetable_ean[u][ v + '_in']['type'] = timetable_ean[u][ v]['type']
    #     timetable_ean[u][v + '_in']['l'] = timetable_ean[u][v]['l']
    #     timetable_ean[u][v + '_in']['u'] = timetable_ean[u][v]['u']
    #     timetable_ean[u][v + '_in']['w'] = timetable_ean[u][v]['w']
    #
    # for v,u in henkel_from:
    #
    #     timetable_ean.add_edge(v + '_out', u)
    #     timetable_ean[ v + '_out'][u]['type'] = timetable_ean[v][u]['type']
    #     timetable_ean[ v + '_out'][u]['l'] = timetable_ean[v][u]['l']
    #     timetable_ean[ v + '_out'][u]['u'] = timetable_ean[v][u]['u']
    #     timetable_ean[ v + '_out'][u]['w'] = timetable_ean[v][u]['w']
    #
    # #timetable_ean.remove_nodes_from(henkel_nodes)
    #
    # print('after removal')
    # for e in timetable_ean.edges():
    #     print(e)



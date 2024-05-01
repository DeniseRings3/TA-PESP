import networkx as nx
#import scripts.DeniseMA.scripts.build_ean.read_ean_functions as rd
import build_ean.read_ean_functions as rd
import copy
def get_line_sequence(ean):
    # ean OHNE headways
    bst_graph_dict ={}
    for c in [ean.subgraph(c).copy() for c in nx.weakly_connected_components(ean)]:
        line = rd.get_line(list(c.nodes())[0])
        bst_graph = nx.DiGraph()
        driving_edges = [(i,j) for (i,j) in c.edges() if (ean[i][j]['type'] == 'driving' or ean[i][j]['type'] == 'henkel-to'
                                                            or ean[i][j]['type'] == 'henkel-from')]
        driving_edges_bst = list(set([(rd.get_station(i),rd.get_station(j)) for (i,j) in driving_edges]))

        bst_graph.add_edges_from(driving_edges_bst)
        bst_graph.remove_edges_from(nx.selfloop_edges(bst_graph))
        bst_graph_dict[line] = bst_graph

    #nx.draw_networkx(bst_graph)
    #plt.show()
    return bst_graph_dict

def get_line_of_sheaf(sheaf,sheaf_dict,alternatives_dict):
    alternative = sheaf_dict[sheaf][0]
    s,t = alternatives_dict[alternative]['s-t-tuple']
    return rd.get_line(s)

def get_sheaf_graph(sheaf, sheaf_dict, alternatives_dict):
    sheaf_graph = nx.DiGraph()
    edges = []
    for F in sheaf_dict[sheaf]:
        edges.extend(alternatives_dict[F]['path'])
    edges = list(set(edges))
    sheaf_graph.add_edges_from(edges)
    return sheaf_graph

def get_line_eans(ean):
    # unterteile in line eans
    line_eans_dict = {}
    S = [ean.subgraph(c).copy() for c in nx.weakly_connected_components(ean)]
    for s in S:
        u, v = list(s.edges)[0]
        line_num = rd.get_line(u)
        # if s.nodes[u]['frequency'] > 1:
        #     #key = str(line_num) +'_'+ str(s.nodes[u]['frequency'])
        #     continue
        line_eans_dict[line_num] = s
    return line_eans_dict

def get_line_dicts(alternatives_dict,sheaf_dict, line):
    new_alternatives_dict = copy.deepcopy(alternatives_dict)
    new_sheaf_dict  = copy.deepcopy(sheaf_dict)
    for F in alternatives_dict:
        if F == 0:
            line_edges = [(i,j) for (i,j) in alternatives_dict[F]['path'] if rd.get_line(i) == line]
            new_alternatives_dict[F]['path'] = line_edges

        else:
            (s,t) = alternatives_dict[F]['s-t-tuple']
           # print(alternatives_dict[F])
            sheaf = alternatives_dict[F]['sheaf_idx']
            if rd.get_line(s) != line:
                new_alternatives_dict.pop(F)
                try:
                    new_sheaf_dict.pop(sheaf)
                except:
                    continue

    return new_alternatives_dict,new_sheaf_dict


from collections import defaultdict, Counter
import csv
import networkx as nx


def get_edges_from_path(path):
    edges = []
    path = path.strip('[')
    path = path.strip(']')
    if len(path) == 0:
        return []

    nodes = path.split(',')

    for index,node in enumerate(nodes):
        node = node.strip()
        node = node.strip('(')
        node = node.strip(')')
        nodes[index] = node

    edges = [tuple(nodes[x:x + 2]) for x in range(0, len(nodes), 2)]

    return edges

def get_s_t_tuple(string):
    if 'inevitable' in string:
        return string,None
    string = string.strip()
    string = string.strip('(')
    string = string.strip(')')
    parts = string.split(',')
    for count,p in enumerate(parts):
        last_ = p.rfind('_')
        if p[last_+1:] == 'in' or p[last_+1:] == 'out':
            parts[count] = p[:last_]

    #print(parts)
    return parts[0].strip(), parts[1].strip()


def read_alternatives(file, sep = ','):
    alternatives_dict = {}
    sheaf_dict = defaultdict(lambda:[])
    sheaf_to_tuple = {}
    with open(file ) as file_obj:
        reader_obj = csv.reader(file_obj, delimiter=sep)
        next(reader_obj)
        # ['alt_idx', 'sheaf_idx', 's-t-tuple', 'weight', 'path']

        for row in reader_obj:
            #print(row)
            row = [i.replace('-', '_') for i in row]

            (s, t) = get_s_t_tuple(row[2])
            path = get_edges_from_path(row[4])
            alternatives_dict[int(row[0])] = {'sheaf_idx': int(row[1]), 's-t-tuple': (s,t), 'weight': int(row[3]), 'path': path }
            sheaf_dict[int(row[1])].append(int(row[0]))
            sheaf_to_tuple[row[1]] = (s,t)
    return alternatives_dict, sheaf_dict, sheaf_to_tuple

def read_shared_infrastructure_file(shared_infrastructure_file):
    curly_H = []
    with open(shared_infrastructure_file) as file_obj:
        reader_obj = csv.reader(file_obj)
        all(next(reader_obj) for i in range(2))
        # ['i', 'j', 'i_bar', 'j_bar']
        for row in reader_obj:
            row = [i.replace('-', '_') for i in row]
            # print(row)
            (i, j) = (row[0], row[1])
            (i_bar, j_bar) = (row[2], row[3])
            if (i!= i_bar) and (j != j_bar):
                curly_H.append(((i, j), (i_bar, j_bar)))
    return curly_H


def extract_event_info(event):
    infos = event.split('_')
    if 'henkel' not in event:
        infos_dict = {'station': infos[0], 'gleis': infos[1], 'gleistyp': infos[2], 'line': infos[3], 'freq_count' : infos[4],
                      'occ_label': infos[5], 'arr_dep': infos[6], 'left_right': infos[7], 'henkel': False}
    else:
        infos_dict = {'station': None,
                      'gleis': None,
                      'gleistyp': None,
                      'line': infos[-3],
                      'freq_count': infos[-2],
                      'occ_label': infos[-1],
                      'arr_dep': None,
                      'left_right': None,
                      'henkel': infos[1]} #henkel id
    return infos_dict

def get_station(event):
    infos = event.split('_')
    if 'henkel' not in event:
        return infos[0]
    else:
        return event

def get_gleis(event):
    infos = event.split('_')
    if 'henkel' not in event:
        return infos[1]
    else:
        return None

def get_gleisbezeichnung(event):
    infos = event.split('_')
    if 'henkel' not in event:
        return infos[0] +'_' + infos[1] +'_'+infos[2]
    else:
        return event


def get_gleistyp(event):
    infos = event.split('_')
    if 'henkel' not in event:
        return infos[2]
    else:
        return 'henkel'

def get_line(event):
    infos = event.split('_')
    if 'henkel' not in event:
        return int(infos[3])
    else:
        return int(infos[-3])

def get_frequ_count(event):
    infos = event.split('_')
    if 'henkel' not in event:
        return int(infos[4])
    else:
        return int(infos[-2])

def get_occ_label(event):
    infos = event.split('_')
    if 'henkel' not in event:
        return int(infos[5])
    else:
        return int(infos[-1])

def get_arr_dep(event):
    infos = event.split('_')
    if 'henkel' not in event:
        return infos[6]
    else:
        return None

def get_direction(event):
    infos = event.split('_')
    if 'henkel' not in event:
        return infos[7]
    else:
        return None
def get_henkel_id(event):
    infos = event.split('_')
    if 'henkel' not in event:
        return None
    else:
        return infos[1]




def build_EAN_from_file(file, sep =','):
    ean = nx.DiGraph()
    node_attributes = {}
    edge_attributes = {}
    edges = []
    with open(file) as file_obj:
        reader_obj = csv.reader(file_obj, delimiter = sep)
        all(next(reader_obj) for i in range(5))
        #['start', 'end', 'type', 'l', 'u', 'w']
        for row in reader_obj:
            if len(row) == 1:
                continue
            elif row[0] == 'start':
                continue

            start = row[0].replace('-','_')
            end = row[1].replace('-','_')

            node_attributes[start] = extract_event_info(start)
            node_attributes[end] = extract_event_info(end)

            edges.append((start, end))
            edge_attributes[(start,end)] = {'type': row[2], 'l': float(row[3]), 'u': float(row[4]), 'w': float(row[5])}

    all_nodes = [i for (i,j) in edge_attributes]
    all_nodes.extend([j for (i,j) in edge_attributes])
    nodes = list(set(all_nodes))
    ean.add_edges_from(edges)



    nx.set_node_attributes(ean, {n: get_station(n) for n in nodes}, 'station')
    nx.set_node_attributes(ean, {n: get_gleis(n) for n in nodes}, 'gleis')
    nx.set_node_attributes(ean, {n: get_gleistyp(n) for n in nodes}, 'gleistyp')
    nx.set_node_attributes(ean, {n: get_line(n) for n in nodes}, 'line')
    nx.set_node_attributes(ean, {n: get_frequ_count(n) for n in nodes}, 'frequency')
    nx.set_node_attributes(ean, {n: get_occ_label(n) for n in nodes}, 'occ_label')
    nx.set_node_attributes(ean, {n: get_arr_dep(n) for n in nodes}, 'arr_dep')
    nx.set_node_attributes(ean, {n: get_direction(n) for n in nodes}, 'direction')
    nx.set_node_attributes(ean, {n: get_henkel_id(n) for n in nodes}, 'henkel_id')
    nx.set_node_attributes(ean, {n: get_gleisbezeichnung(n) for n in nodes}, 'gleisbezeichnung')



    nx.set_edge_attributes(ean, {(i,j): edge_attributes[(i,j)]['type'] for (i,j) in edges}, 'type')
    nx.set_edge_attributes(ean, {(i,j): edge_attributes[(i,j)]['l'] for (i,j) in edges}, 'l')
    nx.set_edge_attributes(ean, {(i,j): edge_attributes[(i,j)]['u'] for (i,j) in edges}, 'u')
    nx.set_edge_attributes(ean, {(i,j): edge_attributes[(i,j)]['w'] for (i,j) in edges}, 'w')

    return ean


def add_headway_arcs(ean, curly_H,  T, epsilon, zugfolge ):
    headway_arcs = []
    headway_attributes = {}

    for ((i,j),(i_bar,j_bar)) in curly_H:
        if i != i_bar and (j != j_bar):
            headway_arcs.append((i,i_bar))
            headway_attributes[(i,i_bar)] = {'type': 'headway', 'l': zugfolge, 'u': T-zugfolge, 'w': 1}

            headway_arcs.append((i_bar, i))
            headway_attributes[(i_bar,i)] = {'type': 'headway', 'l': zugfolge, 'u': T-zugfolge, 'w': 1}

            headway_arcs.append((j, i_bar))
            headway_attributes[(j, i_bar)] = {'type': 'headway', 'l': epsilon, 'u': T - epsilon, 'w': 1}

            headway_arcs.append((j_bar, i))
            headway_attributes[(j_bar, i)] = {'type': 'headway', 'l': epsilon, 'u': T - epsilon, 'w': 1}

        ean.add_edges_from(headway_arcs)
        nx.set_edge_attributes(ean, {(i, j): headway_attributes[(i, j)]['type'] for (i, j) in headway_arcs}, 'type')
        nx.set_edge_attributes(ean, {(i, j): headway_attributes[(i, j)]['l'] for (i, j) in headway_arcs}, 'l')
        nx.set_edge_attributes(ean, {(i, j): headway_attributes[(i, j)]['u'] for (i, j) in headway_arcs}, 'u')
        nx.set_edge_attributes(ean, {(i, j): headway_attributes[(i, j)]['w'] for (i, j) in headway_arcs}, 'w')

    return ean

# name changes
def change_line_in_name(v,new_line,index):
    parts = v.split('_')

    if index < 0:
        index = len(parts) + index

    new_name = parts[0]
    for i in range(1, index):
        new_name += '_' + parts[i]
    new_name += '_' + str(new_line)
    for i in range(index + 1, len(parts)):
        new_name += '_' + parts[i]

    return new_name

def change_full_name(v):
    frequ = get_frequ_count(v)
    parts = v.split('_')
    if 'henkel' in v:
        line = parts[-3]
        new_line = int(str(frequ) + '0' + str(line))
        new_name = change_line_in_name(v, new_line, -3)
    else:
        line = parts[3]
        new_line = int(str(frequ) + '0' + str(line))
        new_name = change_line_in_name(v, new_line, 3)
    return new_name
def change_names_ean(ean):
    new_labels = {}
    for v in ean.nodes:
        if get_frequ_count(v) > 1:
            frequ = get_frequ_count(v)
            parts = v.split('_')
            if 'henkel' in v:
                line = parts[-3]
                new_line = int(str(frequ) + '0' + str(line))
                new_name = change_line_in_name(v, new_line, -3)
            else:
                line = parts[3]
                new_line = int(str(frequ) + '0' + str(line))
                new_name = change_line_in_name(v, new_line, 3)

            ean.nodes[v]['line'] = new_line
            new_labels[v] = new_name
            # print(ean.nodes[v]['line'])


    ean = nx.relabel_nodes(ean, new_labels)
    return ean

def change_names_curlyH(curly_H):
    for index, (edge1, edge2) in enumerate(curly_H):
        new_edge1 = []
        new_edge2 = []
        for i, v in enumerate(edge1):

            if get_frequ_count(v) > 1:
                new_edge1.append(change_full_name(v))
            else:
                new_edge1.append(v)
        for i, v in enumerate(edge2):

            if get_frequ_count(v) > 1:
                new_edge2.append(change_full_name(v))
            else:
                new_edge2.append(v)
        curly_H[index] = (tuple(new_edge1), tuple(new_edge2))
    return curly_H

def change_names_alternatives(alternatives_dict):
    for a in alternatives_dict:
        # print(alternatives_dict[a])
        (s, t) = alternatives_dict[a]['s-t-tuple']


        if 'inevitable' not in s:
            #print(s,t)
            if 'line' in s or 'line' in t:
                alternatives_dict[a]['s-t-tuple'] = (alternatives_dict[a]['path'][0][0], alternatives_dict[a]['path'][-1][-1])
                (s, t) = alternatives_dict[a]['s-t-tuple']
            if get_frequ_count(s) > 1:
                s = change_full_name(s)
            if get_frequ_count(t) > 1:
                t = change_full_name(t)
            alternatives_dict[a]['s-t-tuple'] = (s, t)

        for index, (i, j) in enumerate(alternatives_dict[a]['path']):
            if get_frequ_count(i) > 1:
                i = change_full_name(i)
            if get_frequ_count(j) > 1:
                j = change_full_name(j)

            alternatives_dict[a]['path'][index] = (i, j)
    return  alternatives_dict





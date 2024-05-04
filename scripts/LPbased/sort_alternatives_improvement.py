import math
from collections import defaultdict
from random import sample
import utils.general as util
import build_ean.read_ean_functions as rd
# 1: random

def random_selection(integer_values, ratio, alternatives_dict, sheaf_dict):
    fixed_subset = sample(integer_values, int(ratio * len(integer_values)))
    return fixed_subset

def sorted_by_excluded_alternatives(integer_values, ratio, alternatives_dict, sheaf_dict):
    # sort by anzahl ausgeschlossener alternativen
    temp = []
    for F in integer_values:
        if F == 0:
            continue
        sheaf = alternatives_dict[F]['sheaf_idx']
        temp.append((F, len(sheaf_dict[sheaf])))
    temp = sorted(temp, key=lambda x: x[1], reverse=True)
    temp = [F for (F, length) in temp]
    #temp.insert(0,0)
    print(temp)
    if ratio == 1:
        return temp
    index = math.ceil(len(temp) * ratio)
    non_fixed_subset = temp[index:]
    fixed_subset = temp[:index]
    return fixed_subset

def sorted_by_edges(integer_values, ratio, alternatives_dict, sheaf_dict):
    # sort by anzahl kanten
    temp = []
    for F in integer_values:
        temp.append((F, len(alternatives_dict[F]['path'])))
    temp = sorted(temp, key= lambda x:x[1], reverse=True)
    temp = [F for (F,length) in temp]
    print(temp)
    if ratio == 1:
        return temp
    index = math.ceil(len(temp)*ratio)
    non_fixed_subset = temp[index:]
    fixed_subset = temp[:index]
    return fixed_subset

def sorted_by_headways(integer_values, ratio, alternatives_dict, sheaf_dict,curly_H):
    # sort by activated headways
    temp = []
    for F in integer_values:
        headways = 0
        for (x,y) in alternatives_dict[F]['path']:
            for ((i,j),(i_bar,j_bar)) in curly_H:
                if (i,j) == (x,y) or (i_bar,j_bar) == (x,y):
                    headways += 1
        temp.append((F,headways))

    temp = sorted(temp, key=lambda x: x[1], reverse=True)
    temp = [F for (F, length) in temp]
    print(temp)
    if ratio  == 1:
        return temp
    index = math.ceil(len(temp) * ratio)
    non_fixed_subset = temp[index:]
    fixed_subset = temp[:index]
    return fixed_subset

def sort_by_slack( alternatives_dict, lp_relax_sol,ratio,ean, activated_set = []):
    if activated_set == []:
        activated_set = [F for F in lp_relax_sol['b'] if lp_relax_sol['b'][F] == 1]
    av_slack = []
    for F in activated_set:
        if F == 0:
            continue
        cum = 0
        for (i, j) in alternatives_dict[F]['path']:
            slack = lp_relax_sol['y_bar'][(i, j)] + lp_relax_sol['h'][(i, j)] * ean[i][j]['l']
            cum += slack
        av_slack.append((F, cum / len(alternatives_dict[F]['path'])))

    av_slack = sorted(av_slack, key=lambda x: x[1], reverse=True)
    #print(av_slack)
    temp = [F for (F, length) in av_slack]
    #print(temp)
    if ratio == 1:
        return temp
    index = math.ceil(len(temp) * ratio)
    non_fixed_subset = temp[index:]
    fixed_subset = temp[:index]
    return fixed_subset



def integrality_measures(variable_dict):
    new_integral = 0
    for v in variable_dict:
        new_integral += abs(variable_dict[v] - 0.5)
    new_integral = new_integral/ len(variable_dict)
    return  new_integral

def get_line_of_alternative(F, alternatives_dict, inevitables = False):

    if inevitables:
        lines = []
        for (i,j) in alternatives_dict[F]['path']:
            line = rd.get_line(i)
            lines.append(line)
            return lines
    else:
        (i,j) = alternatives_dict[F]['path'][0]
        return rd.get_line(i)

def sort_by_fractionality(ean_noH,equality_set, alternatives_dict, lp_sol):
    affected_lines = []
    line_alternative_map = defaultdict(lambda: [])
    for F in equality_set:
        if F == 0:
            lines = get_line_of_alternative(F, alternatives_dict, inevitables = True)
            affected_lines.extend(lines)
            for line in lines:
                line_alternative_map[line].append(F)
        else:
            line = get_line_of_alternative(F, alternatives_dict, inevitables = False)
            affected_lines.append(line)
            line_alternative_map[line].append(F)

    affected_lines = list(set(affected_lines))
    print('affected_lines', set(affected_lines))

    line_eans_dict = util.get_line_eans(ean_noH)
   # all_lines = list(line_eans_dict.keys())

    affected_lines_fractionality = []
    for line in affected_lines:
        variable_dict = {}
        #print(line)
        for (i, j) in line_eans_dict[line].edges():
            variable_dict[(i, j)] = lp_sol['h'][(i, j)]
        new_integral = integrality_measures(variable_dict)
        affected_lines_fractionality.append((line, new_integral))
    print('fractionality', affected_lines_fractionality)

    # sort by fractionality:
    affected_lines_fractionality = sorted(affected_lines_fractionality, key=lambda x: x[1], reverse=True)
    affected_lines_fractionality = [line for (line, frac) in affected_lines_fractionality]
    print(affected_lines_fractionality)

    sorted_alternatives = []
    for line in affected_lines_fractionality:
        sorted_alternatives.extend(line_alternative_map[line])

    print(sorted_alternatives)
    return sorted_alternatives

def check_if_abstellgleis_wende(F, alternatives_dict):
    abstellgleis_wende = False
    for (i,j) in alternatives_dict[F]['path']:
        #print(rd.get_gleistyp(i))
        if rd.get_gleistyp(i) == 'A':
            abstellgleis_wende = True

    return abstellgleis_wende

def check_if_henkel_anbindung(F, alternatives_dict):
    henkel_anbindung = False
    for (i,j) in alternatives_dict[F]['path']:
        #print(rd.get_gleistyp(i))
        if rd.get_gleistyp(i) == 'henkel':
            henkel_anbindung = True

    return henkel_anbindung
def custom_sort(alternatives_dict,alternatives_list):
    # fixe handles, abstellgleiswenden
    sorted_list = []
    henkel_anbindungen = [F for F in alternatives_list if check_if_henkel_anbindung(F, alternatives_dict) == True]
    abstellgleis_wende = [F for F in alternatives_list if check_if_abstellgleis_wende(F, alternatives_dict) == True]
    rest = [F for F in alternatives_list if (F not in henkel_anbindungen) and (F not in abstellgleis_wende)]

    sorted_list.extend(henkel_anbindungen)
    sorted_list.extend(abstellgleis_wende)
    sorted_list.extend(rest)
    return sorted_list



import pandas as pd
import numpy as np
from collections import defaultdict, Counter
import csv
import networkx as nx
import openpyxl
import os
from collections import Counter
from ast import literal_eval

from gurobipy.gurobipy import GRB
import os
import LPbased.LPmodel as lp

import json
import timeit
import gurobipy as gp
import time

def find_edge_in_path(path, edge):
    for e in path:
        if e == edge:
            return True
    return False
def h_activation(m,ean,b,h,curlyS, alternatives_dict, special_set = []):
    #S = [F for S in curlyS for F in curlyS[S]]

    # (16)
    if special_set == []:
        edge_set = ean.edges()
    else:
        edge_set = special_set
    for (i,j) in edge_set:
        if ean[i][j]['type'] == 'headway':
            continue
        else:
            m.addConstr(gp.quicksum(b[F] for F in alternatives_dict.keys() if find_edge_in_path(alternatives_dict[F]['path'], (i,j)))
                    <= h[i,j], name='arc_activation_%s%s' %(i,j))
    return m

def sheaf_activation(m,ean,b,h,curlyS, alternatives_dict):
    # (15)
    for sheaf in curlyS:
        m.addConstr(gp.quicksum(b[F] for F in curlyS[sheaf]) == 1, name='sheaf_%s' % sheaf)
    return m

def add_lagrange_objective(m,h,y_bar,ean,b,sheaf_dict,alternatives_dict,lambda_weight, sheaf_relaxation, activation_relaxation,L, obj):
    summation = gp.LinExpr()
    edges_woH = [(i, j) for (i, j) in ean.edges if ean[i][j]['type'] != 'headway']

    for (i, j) in edges_woH:
        summation.add((y_bar[i,j]+ean.edges[i,j]['l']*h[i, j]) * ean.edges[i,j]['w']) # y_bar statt h

    m.addConstr(obj == summation)

    if sheaf_relaxation:
        for sheaf in sheaf_dict:

            temp = gp.LinExpr()
            for F in sheaf_dict[sheaf]:
                temp.add(b[F])

            summation.add(lambda_weight[sheaf]* (1- temp))

            m.addConstr(L[sheaf] == 1 - temp)

    if activation_relaxation:
        for (i, j) in ean.edges():
            if ean[i][j]['type'] == 'headway':
                continue
            else:
                summation.add(lambda_weight[(i,j)] * (gp.quicksum( b[F] for F in alternatives_dict.keys()
                                                     if find_edge_in_path(alternatives_dict[F]['path'], (i, j))) -h[i, j]))

                m.addConstr(L[(i,j)] == gp.quicksum( b[F] for F in alternatives_dict.keys()
                                         if find_edge_in_path(alternatives_dict[F]['path'], (i, j)))-h[i, j])

                m.addConstr(h[i, j] <= gp.quicksum(b[F] for F in alternatives_dict.keys()
                                                              if
                                                               find_edge_in_path(alternatives_dict[F]['path'], (i, j))),
                            name= 'h_inequality_%s_%s' %(i,j))


    m.setObjective(summation, GRB.MINIMIZE)
    return m
def Lagrange_relaxation(modelname, ean, alternatives_dict, T, epsilon, zugfolge, curlyH, curlyS, filename,
                    lambda_weight,
                  sheaf_relaxation =True, activation_relaxation = True,
                  timeout = False,
                 feasibility_stop = False, feasibility_time_limit = 10,
                        gap_stop = False,
                        sol = {}, test_start = False, prio  = False,fixed = [], hard_fix = {}):

    m = gp.Model(modelname)


    edges = [(i, j) for (i, j) in ean.edges] #inkl headway
    edges_woH = [(i, j) for (i, j) in ean.edges if ean[i][j]['type'] != 'headway']
    # set variables

    p = m.addVars(edges, name='p', vtype=GRB.INTEGER, lb=0, ub=1) # upper bound 2 für IB formulation
    pi = m.addVars(ean.nodes(), name='pi', vtype=GRB.CONTINUOUS, lb=0, ub= T - 1)
    y = m.addVars(edges_woH, name='y', vtype=GRB.CONTINUOUS, lb=0)
    y_bar = m.addVars(edges_woH, name='y_bar', vtype=GRB.CONTINUOUS, lb=0)
    h = m.addVars(edges_woH, name='h', vtype=GRB.BINARY, lb=0, ub=1) ##############
    b = m.addVars(alternatives_dict.keys(), name='b', vtype=GRB.BINARY, lb=0, ub=1)


    L = m.addVars(lambda_weight.keys(), name='L', vtype=GRB.CONTINUOUS, lb=-float('inf'), ub=float('inf'))
    obj = m.addVar(name='obj', vtype=GRB.CONTINUOUS)

    m = lp.add_slack_assignment(m, p, pi, y, y_bar, h, ean, T)
    m = lp.add_PESP_constraints(m, p, pi, y, y_bar, h, ean, T)

    m = lp.add_headway_constraints(m, p, pi, h, epsilon, zugfolge, T, curlyH)
    m = lp.fix_henkel(m, ean, pi)

    if (sheaf_relaxation == True) and (activation_relaxation == False):

        m = add_lagrange_objective(m, h, y_bar, ean, b, curlyS, alternatives_dict, lambda_weight, sheaf_relaxation,activation_relaxation,L,obj)
        m = h_activation(m, ean, b, h, curlyS, alternatives_dict)

    elif (sheaf_relaxation == False) and (activation_relaxation == True):
        m = sheaf_activation(m, ean, b, h, curlyS, alternatives_dict)
        m = add_lagrange_objective(m, h, y_bar, ean, b, curlyS, alternatives_dict, lambda_weight,
                                   sheaf_relaxation,activation_relaxation, L, obj)

    elif (sheaf_relaxation == True) and (activation_relaxation == True):
        m = add_lagrange_objective(m, h, y_bar, ean, b, curlyS,alternatives_dict, lambda_weight, sheaf_relaxation,activation_relaxation,L,obj)



    if sol != {}:
        all_variables = [p, pi, y, y_bar, h, b,]
        all_variables_names = ['p', 'pi', 'y', 'y_bar', 'h', 'b', 'delta']
        for index, variable in enumerate(all_variables):
            for i in variable:
                try:
                    variable[i].start = sol[all_variables_names[index]][i]
                    if test_start == True:
                        filename = filename +'_test_feasibility'
                        m.addConstr(variable[i] == sol[all_variables_names[index]][i], name= 'test_start_%s_%s' %all_variables_names[index]%i)

                        m.addConstr(variable[i] == fixed[all_variables_names[index]][i],
                                    name='test_start_%s_%s' % all_variables_names[index] % i)
                except:
                    continue

    #fix oder nur constraint
    if fixed != []:

        m = h_activation(m, ean, b, h, curlyS, alternatives_dict, special_set=fixed)
    if hard_fix != {}:
        for (i,j) in hard_fix:
            m.addConstr(h[(i,j)] == hard_fix[(i,j)], name='fix_prev_%s_%s' %(i,j))

    if sol != {}:
        all_variables = [p, pi, y, y_bar, h, b,]
        all_variables_names = ['p', 'pi', 'y', 'y_bar', 'h', 'b', 'delta']
        for index, variable in enumerate(all_variables):

            for i in variable:
                try:
                    variable[i].start = sol[all_variables_names[index]][i]
                except:
                    continue


    m.write(filename+'.lp')

    if timeout != False:
        m.setParam('TimeLimit', timeout)

    print('log file', filename)
    m.setParam('LogFile', filename +'.log')

    if prio:
        for (i,j) in edges_woH:
            h[(i,j)].BranchPriority = 9


    m._cur_obj = float('inf')
    m._time = time.time()

    # m.computeIIS()
    def feasibility_stop_func(model, where):

        if where == GRB.Callback.MIPNODE:
            sol_count = model.cbGet(GRB.Callback.MIPNODE_SOLCNT)

            if sol_count < 1:
                model._time = time.time()

            if time.time() - model._time > feasibility_time_limit:
                print('stop criterion')
                model.terminate()
        return

    def gap_stop_func(model, where):

        if where == GRB.Callback.MIP:
            obj = model.cbGet(GRB.Callback.MIP_OBJBST)
            bound = model.cbGet(GRB.Callback.MIP_OBJBND)

            gap = abs(obj - bound) / abs(obj)
            if gap > 0.1:
                model._time = time.time()

            if time.time() - model._time > feasibility_time_limit:
                print('stop criterion')
                print('gap', gap)
                model.terminate()
        return

    m._cur_obj = float('inf')
    m._time = time.time()

    if feasibility_stop == True:
        print('feasibility stop')
        print('feasibility time limit', feasibility_time_limit)
        m.optimize(feasibility_stop_func)
    elif gap_stop == True:
        print('gap stop')
        print('feasibility time limit', feasibility_time_limit)
        m.optimize(gap_stop_func)
    else:
        m.optimize()
    runtime = m.Runtime


    if m.status == GRB.INFEASIBLE:
        return m,p,pi,y,y_bar,h,b
        m.feasRelaxS(1, False, False, True)
        m.optimize()
        #m.computeIIS()
        #m.write(filename + "_infeasibility_info.ilp")

    m.printStats()

    try:
        m.write(filename+'.sol')
        all_vars = m.getVars()
        values = m.getAttr("X", all_vars)
        names = m.getAttr("VarName", all_vars)

    except:
        pass



    return m,p,pi,y,y_bar,h,b,L
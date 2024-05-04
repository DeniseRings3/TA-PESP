import math
from random import *
import networkx as nx
import gurobipy as gp
from gurobipy import GRB
import time
import pandas as pd
import os

def feasibility_stop_func(model, where,feasibility_time_limit):
    if where == GRB.Callback.MIP:
        objective = model.cbGet(GRB.Callback.MIP_OBJBST)
    if where == GRB.Callback.MIPSOL:
        sol_count = model.cbGet(GRB.Callback.MIPSOL_OBJ)

        # if objective > N*U*W:
        if sol_count < 1:
            model._time = time.time()

        if time.time() - model._time > feasibility_time_limit:
            print('stop criterion')
            model.terminate()
    return
def add_slack_assignment(m,p,pi,y,y_bar,h,ean, T):
    # only non headway arcs??
    # (AB) variante
    edges_woH = [(i, j) for (i, j) in ean.edges if ean[i][j]['type'] != 'headway']
    for i, j in edges_woH:
        m.addConstr(y[i, j] + ean[i][j]['l'] * h[i, j] == pi[j] - pi[i] + T * p[i, j], name='slack_%s%s' % (i, j))

    # IB formulation
    # m.addConstr(pi[j] - pi[i] + T * p[i, j] == y[i, j] + ean[i][j]['l'], name='slack_%s%s' % (i, j))  # (11) IB formulation, P in 0,1,2
    return m

def add_PESP_constraints(m,p,pi,y,y_bar,h,ean, T):
    edges_woH = [(i, j) for (i, j) in ean.edges if ean[i][j]['type'] != 'headway']
    for i,j in edges_woH:
        m.addConstr(
            y[i, j] <= ean[i][j]['u'] - ean[i][j]['l'] + (T - 1 - ean[i][j]['u'] + ean[i][j]['l']) * (1 - h[i, j]),
            name='artificial_upper_bound_%s%s' % (i, j)) #(12

        m.addConstr(y_bar[i, j] <= (ean[i][j]['u'] - ean[i][j]['l']) * h[i, j], name='upper_bound_coupled_%s%s' % (i, j)) #(13

        m.addConstr(y_bar[i, j] >= y[i, j] - ((T - 1) * (1 - h[i, j])), name='lower_bound_coupled_%s%s' % (i, j)) #(14

    return m

def add_headway_constraints(m,p,pi,h,epsilon,zugfolge,T,curlyH):

    for (i,j),(i_bar,j_bar) in curlyH:
        for (x,y) in [(i,i_bar), (i_bar,i)]:
            m.addConstr(zugfolge*( h[i,j] + h[i_bar,j_bar] - 1) <= pi[y] - pi[x] + T*p[x,y], name='headway_lower_bound_%s%s_%s%s%s%s' % (x,y,i, j,i_bar,j_bar))
            m.addConstr(pi[y] - pi[x] + T*p[x,y] <= (T-zugfolge)*(3 - h[i,j] - h[i_bar,j_bar]) , name='headway_upper_bound_%s%s_%s%s%s%s' % (x,y,i, j,i_bar,j_bar))
            m.addConstr(p[x,y] <= 1,
                        name='modulo_i_%s%s_%s_%s_%s_%s' % (x,y, i, j, i_bar, j_bar))

        for (x,y) in [(j,i_bar), (j_bar,i)]:
            m.addConstr(epsilon*(h[i, j] + h[i_bar, j_bar] - 1) <= pi[y] - pi[x] + T * p[x,y],
                    name= 'headway_lower_bound_%s%s_%s%s%s%s' % (x, y,i, j,i_bar,j_bar))
            m.addConstr(pi[y] - pi[x] + T * p[x,y] <= (T - epsilon)*(3 - h[i, j] - h[i_bar, j_bar]),
                    name= 'headway_upper_bound_%s%s_%s%s%s%s' % (x, y,i, j,i_bar,j_bar))
            m.addConstr(p[x, y] <= 1,
                        name='modulo_i_%s%s_%s_%s_%s_%s' % (x,y, i, j, i_bar, j_bar))


        m.addConstr(-(2 - h[i, j] - h[i_bar, j_bar]) <= p[i, j] + p[j,i_bar] - p[i,i_bar],
                    name='conflict_free_lower_1_%s%s%s%s' % (i, j, i_bar, j_bar))

        m.addConstr(p[i, j] + p[j, i_bar] - p[i, i_bar] <= 2*(2 - h[i,j] - h[i_bar,j_bar]),
                    name='conflict_free_upper_1_%s%s%s%s' % (i, j, i_bar, j_bar))

        m.addConstr(-(2 - h[i, j] - h[i_bar, j_bar]) <= p[i_bar, j_bar] + p[j_bar, i] - p[i_bar, i],
                    name='conflict_free_lower_2_%s%s%s%s' % (i, j, i_bar, j_bar))

        m.addConstr(p[i_bar, j_bar] + p[j_bar, i] - p[i_bar, i] <= 2 * (2 - h[i, j] - h[i_bar, j_bar]),
                    name='conflict_free_upper_2_%s%s%s%s' % (i, j, i_bar, j_bar))

    return m

def add_objective(m,h,y_bar,ean):
    summation = gp.LinExpr()
    edges_woH = [(i, j) for (i, j) in ean.edges if ean[i][j]['type'] != 'headway']
    for (i, j) in edges_woH:
            summation.add((y_bar[i,j]+ean.edges[i,j]['l']*h[i, j]) * ean.edges[i,j]['w']) # y_bar statt h

    m.setObjective(summation, GRB.MINIMIZE)
    return m

def find_edge_in_path(path, edge):
    for e in path:
        if e == edge:
            return True
    return False

def arc_activation(m,ean,b,h,curlyS, alternatives_dict, relaxed = False):
    #S = [F for S in curlyS for F in curlyS[S]]

    # (16)
    for (i,j) in ean.edges():
        if ean[i][j]['type'] == 'headway':
            continue
        else:
            if relaxed:
                m.addConstr(gp.quicksum(b[F] for F in alternatives_dict.keys() if find_edge_in_path(alternatives_dict[F]['path'], (i,j)))
                        <= h[i,j], name='arc_activation_%s%s' %(i,j))
            else:
                m.addConstr(gp.quicksum(
                b[F] for F in alternatives_dict.keys() if find_edge_in_path(alternatives_dict[F]['path'], (i, j)))
                        == h[i, j], name='arc_activation_%s%s' % (i, j))
    return m
def sheaf_activation(m,ean,b,h,curlyS, alternatives_dict):

    # (15)
    for sheaf in curlyS:
        m.addConstr(gp.quicksum(b[F] for F in curlyS[sheaf] ) == 1, name='sheaf_%s' %sheaf)
    return m


def add_heuristics(heuristics_dict, m, ean,p,pi,y,y_bar,h,b):
    for heuristic in heuristics_dict:
        if heuristic == 'common_nodes':
            for node in heuristics_dict['common_nodes']:
                print(node)
                m.addConstr(gp.quicksum(h[i,j] for i,j in ean.edges if ( i == node or j == node)) >= 1, name='fixed_node_%s' % node)

        if heuristic == 'inevitable_nodes':
            for node in heuristics_dict['inevitable_nodes']:
                print('inevitable: ', node)
                m.addConstr(gp.quicksum(h[i,j] for i,j in ean.edges if (i == node or j == node)) >= 1,
                            name='inevitable_node_%s' % node)

        if heuristic == 'common_edges':
            for i,j in heuristics_dict['common_edges']:
                print(i,j)
                m.addConstr(h[i,j] == 1, name='common_edge_%s%s' %(i,j))
    return m

def headway_activation(m,curlyH, h):
    for (i,j),(i_bar,j_bar) in curlyH:
        for (x,y) in [(i, i_bar), (i_bar, i),(j,i_bar), (j_bar,i)]:
            m.addConstr(h[x,y] == h[i,j]*h[i_bar,j_bar], name='headway_activation_%s%s' % (x,y))
    return m

def fix_henkel(m, ean, pi):
    henkel_nodes = [v for v in ean.nodes if 'henkel' in v]
    for v in henkel_nodes:
        m.addConstr(pi[v] == 0, name='fix_henkel_%s' % v)
    return m



def LP_relaxation(modelname, ean, alternatives_dict, T, epsilon, zugfolge, curlyH, curlyS, out_path,timeout = 60*30,
                 feasibility_stop = False, feasibility_time_limit = 30, sol = {}):
    m = gp.Model(modelname)
    #S = [F for S in curlyS for F in curlyS[S]]

    edges = [(i, j) for (i, j) in ean.edges] #inkl headway
    edges_woH = [(i, j) for (i, j) in ean.edges if ean[i][j]['type'] != 'headway']
    # set variables
    p = m.addVars(edges, name='p', vtype=GRB.INTEGER, lb=0, ub=1) # upper bound 2 für IB formulation
    pi = m.addVars(ean.nodes(), name='pi', vtype=GRB.CONTINUOUS, lb=0, ub= T - 1)
    y = m.addVars(edges_woH, name='y', vtype=GRB.CONTINUOUS, lb=0)
    y_bar = m.addVars(edges_woH, name='y_bar', vtype=GRB.CONTINUOUS, lb=0)
    h = m.addVars(edges_woH, name='h', vtype=GRB.CONTINUOUS, lb=0, ub=1)
    b = m.addVars(alternatives_dict.keys(), name='b', vtype=GRB.CONTINUOUS, lb=0, ub=1)

    m = add_objective(m,h,y_bar,ean)
    m = add_slack_assignment(m,p,pi,y,y_bar,h,ean,T)
    m = add_PESP_constraints(m,p,pi,y,y_bar,h,ean,T)
    m = arc_activation(m, ean, b, h, curlyS, alternatives_dict)
    m = sheaf_activation(m, ean, b, h, curlyS, alternatives_dict)
    m = add_headway_constraints(m,p,pi,h,epsilon,zugfolge,T,curlyH)
    m = fix_henkel(m,ean,pi)
    #m = headway_activation(m,curlyH, h)

    if sol != {}:
        all_variables = [p, pi, y, y_bar, h, b,]
        all_variables_names = ['p', 'pi', 'y', 'y_bar', 'h', 'b', 'delta']
        for index, variable in enumerate(all_variables):

            for i in variable:
                try:
                    variable[i].start = sol[all_variables_names[index]][i]
                except:
                    continue

    filename = out_path+ modelname
    m.write(filename+'.lp')
    if timeout != False:
        m.setParam('TimeLimit', timeout)
    m.setParam('LogFile', filename +'.log')

    def cb(model, where):

        sol_count = 0
        if where == GRB.Callback.MIPNODE:
            # Get model objective
            sol_count = model.cbGet(GRB.Callback.MIP_SOLCNT)
            obj = model.cbGet(GRB.Callback.MIPNODE_OBJBST)


            # Has objective changed?
            if abs(obj - model._cur_obj) > 1e-8:
                # If so, update incumbent and time
                model._cur_obj = obj
                model._time = time.time()

        # Terminate if objective has not improved in 20s
        if (time.time() - model._time > 20*60) and (sol_count>1) :
            model.terminate()

    m._cur_obj = float('inf')
    m._time = time.time()
    #m.computeIIS()
    def feasibility_stop_func(model, where, feasibility_time_limit):
        if where == GRB.Callback.MIP:
            objective = model.cbGet(GRB.Callback.MIP_OBJBST)
        if where == GRB.Callback.MIPSOL:
            sol_count = model.cbGet(GRB.Callback.MIPSOL_OBJ)

            #if objective > N*U*W:
            if sol_count < 1:
                model._time = time.time()

            if time.time() - model._time > feasibility_time_limit:
                print('stop criterion')
                model.terminate()
        return


    m._cur_obj = float('inf')
    m._time = time.time()

    if feasibility_stop:
        m.optimize(feasibility_stop_func)
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

        # for v in h.values():
        #     if v.X != 0:
        #         print("{}: {}".format(v.varName, v.X))
    except:
        pass

    # for name, val in zip(names, values):
    #     if val != 0:
    #         print(f"{name} = {val}")

    return m,p,pi,y,y_bar,h,b

# slack assignment standard pesp
# headway q3


def subMIP(modelname, ean, alternatives_dict, T, epsilon, zugfolge, curlyH, curlyS, lp_opt,
           out_path,timeout = 60*30,
                feasibility_stop = False, feasibility_time_limit = 30, sol = {}, fixed_subset = [],
           filename = '',relaxed = False,
           no_improvement_stop = True):
    m = gp.Model(modelname)
    #S = [F for S in curlyS for F in curlyS[S]]

    edges = [(i, j) for (i, j) in ean.edges] #inkl headway
    edges_woH = [(i, j) for (i, j) in ean.edges if ean[i][j]['type'] != 'headway']
    # set variables
    p = m.addVars(edges, name='p', vtype=GRB.INTEGER, lb=0, ub=1) # upper bound 2 für IB formulation
    pi = m.addVars(ean.nodes(), name='pi', vtype=GRB.CONTINUOUS, lb=0, ub= T - 1)
    y = m.addVars(edges_woH, name='y', vtype=GRB.CONTINUOUS, lb=0)
    y_bar = m.addVars(edges_woH, name='y_bar', vtype=GRB.CONTINUOUS, lb=0)
    h = m.addVars(edges_woH, name='h', vtype=GRB.BINARY, lb=0, ub=1)
    b = m.addVars(alternatives_dict.keys(), name='b', vtype=GRB.BINARY)


    for F in fixed_subset:
        m.addConstr(math.floor(lp_opt[F]) <= b[F])
        m.addConstr(b[F] <= math.ceil(lp_opt[F]))


    m = add_objective(m,h,y_bar,ean)
    m = add_slack_assignment(m,p,pi,y,y_bar,h,ean,T)
    m = add_PESP_constraints(m,p,pi,y,y_bar,h,ean,T)
    m = arc_activation(m, ean, b, h, curlyS, alternatives_dict, relaxed)
    m = sheaf_activation(m, ean, b, h, curlyS, alternatives_dict)
    m = add_headway_constraints(m,p,pi,h,epsilon,zugfolge,T,curlyH)
    m = fix_henkel(m,ean,pi)
    #m = headway_activation(m,curlyH, h)

    if sol != {}:
        all_variables = [p, pi, y, y_bar, h, b,]
        all_variables_names = ['p', 'pi', 'y', 'y_bar', 'h', 'b', 'delta']
        for index, variable in enumerate(all_variables):

            for i in variable:
                try:
                    variable[i].start = sol[all_variables_names[index]][i]
                except:
                    continue

    if filename == '':
        filename = out_path+ modelname+'_subMBP'
    m.write(filename+'.lp')
    if timeout != False:
        m.setParam('TimeLimit', timeout)

    m.setParam('LogFile', filename +'.log')

    m._cur_obj = -100
    m._time = time.time()
    m._prev_obj = -100
    # m.computeIIS()
    def feasibility_stop_func(model, where):
        # if where == GRB.Callback.MIP:
        #     objective = model.cbGet(GRB.Callback.MIP_OBJBST)
        if where == GRB.Callback.MIPSOL:
            sol_count = model.cbGet(GRB.Callback.MIPSOL_SOLCNT)
            # if objective > N*U*W:
            if sol_count < 1:
                model._time = time.time()

            if time.time() - model._time > feasibility_time_limit:
                print('stop criterion')
                model.terminate()
        return

    def no_improvement_func(model, where):
        if where == GRB.Callback.MIP:
            objective = model.cbGet(GRB.Callback.MIP_OBJBST)
            #sol_count = model.cbGet(GRB.Callback.MIPSOL_SOLCNT)

            # if where == GRB.Callback.MIPSOL:

            sol_count = model.cbGet(GRB.Callback.MIP_SOLCNT)

            try:

                objective = round(model.cbGet(GRB.Callback.MIP_OBJBST), 2)
            except:
                objective = -100




            if (sol_count == 0) or (objective != m._prev_obj):

                model._time = time.time()


            elif time.time() - model._time > 10 * 60:
                print('stop criterion')
                model.terminate()

            m._prev_obj = objective
        return

    if feasibility_stop:
        m.optimize(feasibility_stop_func)
    elif no_improvement_stop:
        m.optimize(no_improvement_func)
    else:
        m.optimize()
    runtime = m.Runtime

    if m.status == GRB.INFEASIBLE:
        return m, p, pi, y, y_bar, h, b
        #m.feasRelaxS(1, False, False, True)
        #m.optimize()
        m.computeIIS()
        m.write(filename + "_infeasibility_info.ilp")


    m.printStats()

    try:
        m.write(filename+'.sol')
        all_vars = m.getVars()
        values = m.getAttr("X", all_vars)
        names = m.getAttr("VarName", all_vars)

        # for v in h.values():
        #     if v.X != 0:
        #         print("{}: {}".format(v.varName, v.X))
    except:
        pass

    return m,p,pi,y,y_bar,h,b

def RINS_subMIP(modelname, ean, alternatives_dict, T, epsilon, zugfolge, curlyH, curlyS,
                lp_opt,mip_sol, equality_set, rins_epsilon,
           out_path,timeout = 60*30,feasibility_stop = False, feasibility_time_limit = 30, sol = {}, fixed_subset = [],
                filename = '',relaxed = False,
                no_improvement_stop = False):
    m = gp.Model(modelname)
    #S = [F for S in curlyS for F in curlyS[S]]

    edges = [(i, j) for (i, j) in ean.edges] #inkl headway
    edges_woH = [(i, j) for (i, j) in ean.edges if ean[i][j]['type'] != 'headway']
    # set variables
    p = m.addVars(edges, name='p', vtype=GRB.INTEGER, lb=0, ub=1) # upper bound 2 für IB formulation
    pi = m.addVars(ean.nodes(), name='pi', vtype=GRB.CONTINUOUS, lb=0, ub= T - 1)
    y = m.addVars(edges_woH, name='y', vtype=GRB.CONTINUOUS, lb=0)
    y_bar = m.addVars(edges_woH, name='y_bar', vtype=GRB.CONTINUOUS, lb=0)
    h = m.addVars(edges_woH, name='h', vtype=GRB.BINARY, lb=0, ub=1)
    b = m.addVars(alternatives_dict.keys(), name='b', vtype=GRB.BINARY)

    # if relaxed_version == True:
    #     # only fix for a subset of integer variables
    #     integer_values = [F for F in lp_opt if (lp_opt[F] == 0 or lp_opt[F] == 1) ]
    #     print(integer_values)
    #
    #     non_fixed_subset = sample(equality_set, int(0.5 * len(equality_set)))
    for F in fixed_subset:
        #if F not in non_fixed_subset:
        m.addConstr(b[F] == mip_sol['b'][F],name='fix_alt_%s' % F )
    # else:
    #     for F in equality_set:
    #             m.addConstr(b[F] == mip_sol['b'][F],name='fix_alt_%s' % F )


    # objective cut-off
    cT_x = gp.LinExpr()
    edges_woH = [(i, j) for (i, j) in ean.edges if ean[i][j]['type'] != 'headway']
    for (i, j) in edges_woH:
        cT_x.add((y_bar[i, j] + ean.edges[i, j]['l'] * h[i, j]) * ean.edges[i, j]['w'])  # y_bar statt h

    cT_x_tilde = gp.LinExpr()
    edges_woH = [(i, j) for (i, j) in ean.edges if ean[i][j]['type'] != 'headway']
    for (i, j) in edges_woH:
        cT_x_tilde.add((mip_sol['y_bar'][i, j] + ean.edges[i, j]['l'] * mip_sol['h'][i, j]) * ean.edges[i, j]['w'])  # y_bar statt h

    m.addConstr(cT_x <= (1- rins_epsilon)*cT_x_tilde, name='objective_cutoff')
    #

    m = add_objective(m,h,y_bar,ean)
    m = add_slack_assignment(m,p,pi,y,y_bar,h,ean,T)
    m = add_PESP_constraints(m,p,pi,y,y_bar,h,ean,T)
    m = sheaf_activation(m, ean, b, h, curlyS, alternatives_dict)
    m = arc_activation(m, ean, b, h, curlyS, alternatives_dict, relaxed)
    m = add_headway_constraints(m,p,pi,h,epsilon,zugfolge,T,curlyH)
    m = fix_henkel(m,ean,pi)
    #m = headway_activation(m,curlyH, h)

    if sol != {}:
        all_variables = [p, pi, y, y_bar, h, b,]
        all_variables_names = ['p', 'pi', 'y', 'y_bar', 'h', 'b', 'delta']
        for index, variable in enumerate(all_variables):

            for i in variable:
                try:
                    variable[i].start = sol[all_variables_names[index]][i]
                except:
                    continue

    if filename == '':
        filename = out_path+ modelname+'_subMBP'
    m.write(filename+'.lp')
    if timeout != False:
        m.setParam('TimeLimit', timeout)

    m.setParam('LogFile', filename +'.log')

    m._cur_obj = float('inf')
    m._time = time.time()
    #m.computeIIS()

    m._cur_obj = float('inf')
    m._time = time.time()
    m._prev_obj = float('inf')

    # m.computeIIS()
    def feasibility_stop_func(model, where, feasibility_time_limit):
        if where == GRB.Callback.MIP:
            objective = model.cbGet(GRB.Callback.MIP_OBJBST)
        if where == GRB.Callback.MIPSOL:
            sol_count = model.cbGet(GRB.Callback.MIPSOL_OBJ)

            # if objective > N*U*W:
            if sol_count < 1:
                model._time = time.time()

            if time.time() - model._time > feasibility_time_limit:
                print('stop criterion')
                model.terminate()
        return

    def no_improvement_func(model, where):
        if where == GRB.Callback.MIP:
            objective = model.cbGet(GRB.Callback.MIP_OBJBST)

        #if where == GRB.Callback.MIPSOL:

            sol_count = model.cbGet(GRB.Callback.MIP_SOLCNT)
            try:
                objective = round(model.cbGet(GRB.Callback.MIP_OBJBST), 2)
            except:
                objective = -100


            if (sol_count == 0)  or (objective != m._prev_obj):
                model._time = time.time()

            elif time.time() - model._time > 10*60:
                print('stop criterion')
                model.terminate()
            m._prev_obj = objective
        return

    if feasibility_stop:
        m.optimize(feasibility_stop_func)

    elif no_improvement_stop:
        m.optimize(no_improvement_func)
    else:
        m.optimize()
    runtime = m.Runtime

    if m.status == GRB.INFEASIBLE:

        #m.feasRelaxS(1, False, False, True)
        #m.optimize()
        #m.computeIIS()
        #m.write(filename + "_infeasibility_info.ilp")
        return m, p, pi, y, y_bar, h, b

    m.printStats()

    try:
        m.write(filename+'.sol')
        all_vars = m.getVars()
        values = m.getAttr("X", all_vars)
        names = m.getAttr("VarName", all_vars)

        # for v in h.values():
        #     if v.X != 0:
        #         print("{}: {}".format(v.varName, v.X))
    except:
        pass

    return m,p,pi,y,y_bar,h,b

def add_penalized_rins_objective(m,h,y_bar,ean, mip_sol, rins_epsilon):
    summation = gp.LinExpr()
    # edges_woH = [(i, j) for (i, j) in ean.edges if ean[i][j]['type'] != 'headway']
    # for (i, j) in edges_woH:
    #     summation.add((y_bar[i, j] + ean.edges[i, j]['l'] * h[i, j]) * ean.edges[i, j]['w'])  # y_bar statt h
    #
    # m.setObjective(summation, GRB.MINIMIZE)

    # objective cut-off
    cT_x = gp.LinExpr()
    edges_woH = [(i, j) for (i, j) in ean.edges if ean[i][j]['type'] != 'headway']
    for (i, j) in edges_woH:
        cT_x.add((y_bar[i, j] + ean.edges[i, j]['l'] * h[i, j]) * ean.edges[i, j]['w'])  # y_bar statt h

    cT_x_tilde = gp.LinExpr()
    edges_woH = [(i, j) for (i, j) in ean.edges if ean[i][j]['type'] != 'headway']
    for (i, j) in edges_woH:
        cT_x_tilde.add((mip_sol['y_bar'][i, j] + ean.edges[i, j]['l'] * mip_sol['h'][i, j]) * ean.edges[i, j][
            'w'])  # y_bar statt h

    #summation.add(cT_x -(1 - rins_epsilon) * cT_x_tilde)
    summation.add(cT_x)


    #m.addConstr(cT_x <= (1 - rins_epsilon) * cT_x_tilde, name='objective_cutoff')
    m.setObjective(summation, GRB.MINIMIZE)
    return m

def penalized_RINS(modelname, ean, alternatives_dict, T, epsilon, zugfolge, curlyH, curlyS,
                lp_opt,mip_sol, equality_set, rins_epsilon,
           out_path,timeout = 60*30,feasibility_stop = False, feasibility_time_limit = 30, sol = {}, non_fixed_subset = []):
    m = gp.Model(modelname)
    #S = [F for S in curlyS for F in curlyS[S]]

    edges = [(i, j) for (i, j) in ean.edges] #inkl headway
    edges_woH = [(i, j) for (i, j) in ean.edges if ean[i][j]['type'] != 'headway']
    # set variables
    p = m.addVars(edges, name='p', vtype=GRB.INTEGER, lb=0, ub=1) # upper bound 2 für IB formulation
    pi = m.addVars(ean.nodes(), name='pi', vtype=GRB.CONTINUOUS, lb=0, ub= T - 1)
    y = m.addVars(edges_woH, name='y', vtype=GRB.CONTINUOUS, lb=0)
    y_bar = m.addVars(edges_woH, name='y_bar', vtype=GRB.CONTINUOUS, lb=0)
    h = m.addVars(edges_woH, name='h', vtype=GRB.CONTINUOUS, lb=0, ub=1)
    b = m.addVars(alternatives_dict.keys(), name='b', vtype=GRB.BINARY)

    # if relaxed_version == True:
    #     # only fix for a subset of integer variables
    #     integer_values = [F for F in lp_opt if (lp_opt[F] == 0 or lp_opt[F] == 1) ]
    #     print(integer_values)
    #
    #     non_fixed_subset = sample(equality_set, int(0.5 * len(equality_set)))
    for F in equality_set:
        if F not in non_fixed_subset:
            m.addConstr(b[F] == mip_sol['b'][F],name='fix_alt_%s' % F )
    # else:
    #     for F in equality_set:
    #             m.addConstr(b[F] == mip_sol['b'][F],name='fix_alt_%s' % F )




    m = add_penalized_rins_objective(m,h,y_bar,ean,mip_sol,rins_epsilon)
    m = add_slack_assignment(m,p,pi,y,y_bar,h,ean,T)
    m = add_PESP_constraints(m,p,pi,y,y_bar,h,ean,T)
    m = arc_activation(m, ean, b, h, curlyS, alternatives_dict)
    m = add_headway_constraints(m,p,pi,h,epsilon,zugfolge,T,curlyH)
    m = fix_henkel(m,ean,pi)
    #m = headway_activation(m,curlyH, h)

    if sol != {}:
        all_variables = [p, pi, y, y_bar, h, b,]
        all_variables_names = ['p', 'pi', 'y', 'y_bar', 'h', 'b', 'delta']
        for index, variable in enumerate(all_variables):

            for i in variable:
                try:
                    variable[i].start = sol[all_variables_names[index]][i]
                except:
                    continue

    filename = out_path+ modelname+'_subMBP'
    m.write(filename+'.lp')
    if timeout != False:
        m.setParam('TimeLimit', timeout)

    m.setParam('LogFile', filename +'.log')

    m._cur_obj = float('inf')
    m._time = time.time()
    #m.computeIIS()

    m._cur_obj = float('inf')
    m._time = time.time()

    # m.computeIIS()
    def feasibility_stop_func(model, where, feasibility_time_limit):
        if where == GRB.Callback.MIP:
            objective = model.cbGet(GRB.Callback.MIP_OBJBST)
        if where == GRB.Callback.MIPSOL:
            sol_count = model.cbGet(GRB.Callback.MIPSOL_OBJ)

            # if objective > N*U*W:
            if sol_count < 1:
                model._time = time.time()

            if time.time() - model._time > feasibility_time_limit:
                print('stop criterion')
                model.terminate()
        return

    if feasibility_stop:
        m.optimize(feasibility_stop_func)
    else:
        m.optimize()
    runtime = m.Runtime

    if m.status == GRB.INFEASIBLE:

        #m.feasRelaxS(1, False, False, True)
        #m.optimize()
        #m.computeIIS()
        #m.write(filename + "_infeasibility_info.ilp")
        return m, p, pi, y, y_bar, h, b

    m.printStats()

    try:
        m.write(filename+'.sol')
        all_vars = m.getVars()
        values = m.getAttr("X", all_vars)
        names = m.getAttr("VarName", all_vars)

        # for v in h.values():
        #     if v.X != 0:
        #         print("{}: {}".format(v.varName, v.X))
    except:
        pass

    return m,p,pi,y,y_bar,h,b

def arc_activation_subMIP(m, ean, b_J, b_I, h, curlyS, alternatives_dict, IntegerSet):

# (15)
    for sheaf in curlyS:
        summation = gp.LinExpr()
        IntegerAlternatives = [F for F in curlyS[sheaf] if F in IntegerSet]
        NonIntegerAlternatives = [F for F in curlyS[sheaf] if F not in IntegerSet]


        for F in curlyS[sheaf]:
            if F in IntegerAlternatives:
                summation.add(b_I[F])
            else:
                summation.add(b_J[F])

        m.addConstr(summation == 1,name='sheaf_%s' % sheaf)
    # (16)

    for (i, j) in ean.edges():
        if ean[i][j]['type'] == 'headway':
            continue
        else:
            summation = gp.LinExpr()
            for F in alternatives_dict.keys():
                if find_edge_in_path(alternatives_dict[F]['path'], (i, j)):
                    if F in IntegerSet:
                        summation.add(b_I[F])
                    else:
                        summation.add(b_J[F])

            m.addConstr(summation == h[i, j], name='arc_activation_%s%s' % (i, j))

    return m
def evaluate_log(gurobilogfile):
    size = {}
    solution_count = -10
    time_out = False
    presolved = False

    with open(gurobilogfile) as f:
        for line in f:
            if "Presolved" in line:
                presolved = True

            if "Optimize a model" in line:
                strings = line.split()
                #print(strings)
                r = strings.index('rows,')
                c = strings.index('columns')
                n = strings.index('nonzeros')
                #print(r)
                size['rows'] = strings[r-1]
                size['columns'] = strings[c - 1]
                size['nonzeros'] = strings[n - 1]

            if "Variable types:" in line and (presolved is not True):
                strings = line.split()
                print(strings)
                cont = strings.index('continuous,')
                int = strings.index('integer')
                bin = strings.index('binary)')
                size['variables continuous'] = strings[cont - 1]
                size['variables integer'] = strings[int - 1]
                size['variables binary'] = strings[bin - 1].strip('(')

            if "Solution count" in line:
                strings = line.split()
                solution_count = strings[2].strip(':')
                size['solution count'] = solution_count

            if "Time limit reached" in line:
                time_out = True

            if "Best objective" in line:
                strings = line.split()
                obj = strings.index('objective')
                best_obj = strings[obj + 1].strip(',')
                size['best objective'] = best_obj
                bound = strings.index('bound')
                best_bound = strings[bound + 1].strip(',')
                size['best bound'] = best_bound
                gap = strings.index('gap')
                best_gap = strings[gap + 1]
                size['best gap'] = best_gap


    return size


def analyse_solution(m):
    all_vars = m.getVars()
    values = m.getAttr("X", all_vars)
    names = m.getAttr("VarName", all_vars)
    df = pd.DataFrame({'names':names, 'values': values})
    return df
    # nonzeros = []
    # for name, val in zip(names, values):
    #     if val != 0:
    #         nonzeros.append((name,val))



import networkx as nx
import gurobipy as gp
from gurobipy import GRB
import time
import pandas as pd
import os

def find_edge_in_path(path, edge):
    for e in path:
        if e == edge:
            return True
    return False
def add_slack_assignment(m,p,pi,y,y_bar,h,ean, T):
    # ( 3.5)
    # AB Formulation
    edges_woH = [(i, j) for (i, j) in ean.edges if ean[i][j]['type'] != 'headway']
    for i, j in edges_woH:
        m.addConstr(y[i, j] + ean[i][j]['l'] * h[i, j] == pi[j] - pi[i] + T * p[i, j], name='slack_%s%s' % (i, j))

    # IB formulation
    # m.addConstr(pi[j] - pi[i] + T * p[i, j] == y[i, j] + ean[i][j]['l'], name='slack_%s%s' % (i, j))  # (11) IB formulation, P in 0,1,2
    return m

def add_PESP_constraints(m,p,pi,y,y_bar,h,ean, T):
    edges_woH = [(i, j) for (i, j) in ean.edges if ean[i][j]['type'] != 'headway']
    for i,j in edges_woH:
        # ( 3.6)
        m.addConstr(y[i, j] <= ean[i][j]['u'] - ean[i][j]['l'] + (T - 1 - ean[i][j]['u'] + ean[i][j]['l']) * (1 - h[i, j]),
            name='artificial_upper_bound_%s%s' % (i, j)) #(12

        # ( 3.7)
        m.addConstr(y_bar[i, j] <= (ean[i][j]['u'] - ean[i][j]['l']) * h[i, j], name='upper_bound_coupled_%s%s' % (i, j)) #(13

        # ( 3.8)
        m.addConstr(y_bar[i, j] >= y[i, j] - ((T - 1) * (1 - h[i, j])), name='lower_bound_coupled_%s%s' % (i, j)) #(14

    return m

def add_headway_constraints(m,p,pi,h,epsilon,zugfolge,T,curlyH):
    for (i,j),(i_bar,j_bar) in curlyH:
        for (x,y) in [(i,i_bar), (i_bar,i)]:

            # (3.18 )
            m.addConstr(zugfolge*( h[i,j] + h[i_bar,j_bar] - 1) <= pi[y] - pi[x] + T*p[x,y],
                        name='headway_lower_bound_%s%s_%s%s%s%s' % (x,y,i, j,i_bar,j_bar))
            m.addConstr(pi[y] - pi[x] + T*p[x,y] <= (T-zugfolge)*(3 - h[i,j] - h[i_bar,j_bar]) ,
                        name='headway_upper_bound_%s%s_%s%s%s%s' % (x,y,i, j,i_bar,j_bar))
            m.addConstr(p[x,y] <= 1,
                        name='modulo_i_%s%s_%s_%s_%s_%s' % (x,y, i, j, i_bar, j_bar))

        # (3.19)
        for (x,y) in [(j,i_bar), (j_bar,i)]:
            m.addConstr(epsilon*(h[i, j] + h[i_bar, j_bar] - 1) <= pi[y] - pi[x] + T * p[x,y],
                    name= 'headway_eps_lower_bound_%s%s_%s%s%s%s' % (x, y,i, j,i_bar,j_bar))
            m.addConstr(pi[y] - pi[x] + T * p[x,y] <= (T - epsilon)*(3 - h[i, j] - h[i_bar, j_bar]),
                    name= 'headway_eps_upper_bound_%s%s_%s%s%s%s' % (x, y,i, j,i_bar,j_bar))
            m.addConstr(p[x, y] <= 1,
                        name='modulo_i_%s%s_%s_%s_%s_%s' % (x,y, i, j, i_bar, j_bar))

        # (3.20)
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



def arc_activation(m,ean,b,h,curlyS, alternatives_dict, relaxed):

    # (16)
    for (i,j) in ean.edges():
        if ean[i][j]['type'] == 'headway':
            continue
        else:
            if relaxed:
                # inequality formulation of (3.10)
                m.addConstr(gp.quicksum(b[F] for F in alternatives_dict.keys() if find_edge_in_path(alternatives_dict[F]['path'], (i,j)))
                        <= h[i,j], name='arc_activation_%s%s' %(i,j))
            else:
                # equality formulation of (3.11)
                m.addConstr(gp.quicksum(
                b[F] for F in alternatives_dict.keys() if find_edge_in_path(alternatives_dict[F]['path'], (i, j)))
                        == h[i, j], name='arc_activation_%s%s' % (i, j))
    return m

def sheaf_activation(m,ean,b,h,curlyS, alternatives_dict):
    # (3.9)
    for sheaf in curlyS:
        m.addConstr(gp.quicksum(b[F] for F in curlyS[sheaf] ) == 1, name='sheaf_%s' %sheaf)
    return m


def fix_henkel(m, ean, pi):
    henkel_nodes = [v for v in ean.nodes if 'henkel' in v]
    for v in henkel_nodes:
        m.addConstr(pi[v] == 0, name='fix_henkel_%s' % v)
    return m



def set_up_model(modelname, ean, alternatives_dict, T, epsilon, zugfolge, curlyH, curlyS,
                 out_path,timeout = 60*30,
                 feasibility_stop = False, feasibility_time_limit = 30, sol = {},
                 test_start = False, filename = '', relaxed = False,
                 no_improvement_stop = True):

    m = gp.Model(modelname)

    edges = [(i, j) for (i, j) in ean.edges] #inkl headway
    edges_woH = [(i, j) for (i, j) in ean.edges if ean[i][j]['type'] != 'headway']

    # set variables
    p = m.addVars(edges, name='p', vtype=GRB.INTEGER, lb=0, ub=1)
    pi = m.addVars(ean.nodes(), name='pi', vtype=GRB.CONTINUOUS, lb=0, ub= T - 1)
    y = m.addVars(edges_woH, name='y', vtype=GRB.CONTINUOUS, lb=0)
    y_bar = m.addVars(edges_woH, name='y_bar', vtype=GRB.CONTINUOUS, lb=0)
    h = m.addVars(edges_woH, name='h', vtype=GRB.BINARY, lb=0, ub=1)
    b = m.addVars(alternatives_dict.keys(), name='b', vtype=GRB.BINARY)

    m = add_objective(m,h,y_bar,ean)

    # add constraints
    m = add_slack_assignment(m,p,pi,y,y_bar,h,ean,T)
    m = add_PESP_constraints(m,p,pi,y,y_bar,h,ean,T)
    m = arc_activation(m, ean, b, h, curlyS, alternatives_dict, relaxed)
    m = add_headway_constraints(m,p,pi,h,epsilon,zugfolge,T,curlyH)
    m = fix_henkel(m,ean,pi)
    m = sheaf_activation(m, ean, b, h, curlyS, alternatives_dict)


    # set solution if provided
    if sol != {}:
        all_variables = [p, pi, y, y_bar, h, b,]
        all_variables_names = ['p', 'pi', 'y', 'y_bar', 'h', 'b']
        for index, variable in enumerate(all_variables):
            for i in variable:
                # test to check if given solution is feasible
                if test_start == True:
                    m.addConstr(variable[i] == sol[all_variables_names[index]][i],
                                name='test_start_%s_%s' % (all_variables_names[index],i))
                try:
                    variable[i].start = sol[all_variables_names[index]][i]

                except:
                    continue

    if filename == '':
        filename = out_path+ modelname

    m.write(filename+'.lp')

    if timeout != False:
        m.setParam('TimeLimit', timeout)

    m.setParam('LogFile', filename +'.log')


    m._cur_obj = float('inf')
    m._time = time.time()
    m._prev_obj = float('inf')

    def feasibility_stop_func(model, where):
        if where == GRB.Callback.MIP:
            objective = model.cbGet(GRB.Callback.MIP_OBJBST)
        if where == GRB.Callback.MIPSOL:
            sol_count = sol_count = model.cbGet(GRB.Callback.MIPSOL_SOLCNT)

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

            # if where == GRB.Callback.MIPSOL:

            # sol_count = model.cbGet(GRB.Callback.MIPSOL_SOLCNT)
            try:
                objective = round(model.cbGet(GRB.Callback.MIP_OBJBST), 2)
            except:
                objective = -100

            if (objective == -100) or (objective != m._prev_obj):
                model._time = time.time()

            if time.time() - model._time > 20 * 60:
                print('stop criterion')
                model.terminate()
            m._prev_obj = objective
        return


    m._cur_obj = float('inf')
    m._time = time.time()

    if feasibility_stop == True:
        print('feasibility stop')
        print('feasibility time limit', feasibility_time_limit)
        m.optimize(feasibility_stop_func)

    elif no_improvement_stop == True:
        print('plateau stop')
        print('time limit', feasibility_time_limit)
        m.optimize(no_improvement_func)

    else:
        m.optimize()

    runtime = m.Runtime

    if m.status == GRB.INFEASIBLE:
        print('infeasible')
        m.computeIIS()
        m.write(filename + "_infeasibility_info.ilp")
        return m, p, pi, y, y_bar, h, b

    m.printStats()

    try:
        m.write(filename+'.sol')
        all_vars = m.getVars()
        values = m.getAttr("X", all_vars)
        names = m.getAttr("VarName", all_vars)

        for v in h.values():
            if v.X != 0:
                print("{}: {}".format(v.varName, v.X))
    except:
        pass

    return m,p,pi,y,y_bar,h,b


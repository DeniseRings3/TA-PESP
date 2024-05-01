import math
from random import *

import networkx as nx
import gurobipy as gp
from gurobipy import GRB
import time
import pandas as pd
import os
#import scripts.DeniseMA.scripts.model.BuildModel as bm
import model.BuildModel as bm
def branching_MIP(modelname, ean, alternatives_dict, T, epsilon, zugfolge, curlyH, curlyS,
                lp_opt, mip_sol, equality_set,
           out_path,timeout = 60*30,feasibility_stop = False, feasibility_time_limit = 30, sol = {}, non_fixed_subset = [],
                filename = '', relaxed = False,mip_objective =0, iteration_timeout = 3*60,
                  improvement_stop = True):
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
        m.addConstr(b[F] == lp_opt['b'][F],name='fix_alt_%s' % F )


    # objective cut-off
    # cT_x = gp.LinExpr()
    # edges_woH = [(i, j) for (i, j) in ean.edges if ean[i][j]['type'] != 'headway']
    # for (i, j) in edges_woH:
    #     cT_x.add((y_bar[i, j] + ean.edges[i, j]['l'] * h[i, j]) * ean.edges[i, j]['w'])  # y_bar statt h
    #
    # cT_x_tilde = gp.LinExpr()
    # edges_woH = [(i, j) for (i, j) in ean.edges if ean[i][j]['type'] != 'headway']
    # for (i, j) in edges_woH:
    #     cT_x_tilde.add((mip_sol['y_bar'][i, j] + ean.edges[i, j]['l'] * mip_sol['h'][i, j]) * ean.edges[i, j]['w'])  # y_bar statt h
    #
    # m.addConstr(cT_x <= (1- rins_epsilon)*cT_x_tilde, name='objective_cutoff')
    #

    m = bm.add_objective(m,h,y_bar,ean)
    m = bm.add_slack_assignment(m,p,pi,y,y_bar,h,ean,T)
    m = bm.add_PESP_constraints(m,p,pi,y,y_bar,h,ean,T)
    m = bm.arc_activation(m, ean, b, h, curlyS, alternatives_dict, relaxed)
    m = bm.sheaf_activation(m, ean, b, h, curlyS, alternatives_dict)
    m = bm.add_headway_constraints(m,p,pi,h,epsilon,zugfolge,T,curlyH)
    m = bm.fix_henkel(m,ean,pi)


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
    m._start_time = time.time()
    #m.computeIIS()

    m._cur_obj = float('inf')
    m._time = time.time()

    m._prev_obj = float('inf')
    m._stopping_type = False

    def improvement_func(model, where):
        if where == GRB.Callback.MIP:
            objective = model.cbGet(GRB.Callback.MIP_OBJBST)
            sol_count = model.cbGet(GRB.Callback.MIP_SOLCNT)

            try:

                objective = round(model.cbGet(GRB.Callback.MIP_OBJBST), 2)
            except:
                objective = -100




            if (sol_count == 0) or objective > 0.97 * mip_objective :
                model._time = time.time()

                if model._time- model._start_time > iteration_timeout:
                    print('stop criterion iteration timoeut')
                    m._stopping_type = 'no improvement'
                    model.terminate()



            elif time.time() - model._time > 10 * 60:
                print('stop criterion plateau')
                model._stopping_type = 'plateau stop'
                model.terminate()

            m._prev_obj = objective
        return

    # m.computeIIS()
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


    if feasibility_stop:
        m.optimize(feasibility_stop_func)
        #m.optimize(no_improvement_func)
    if improvement_stop:
        m.optimize(improvement_func)
    else:
        m.optimize()
    runtime = m.Runtime

    if m.status == GRB.INFEASIBLE:

        #m.feasRelaxS(1, False, False, True)
        #m.optimize()
        #m.computeIIS()
        #m.write(filename + "_infeasibility_info.ilp")
        return m, p, pi, y, y_bar, h, b, m._stopping_type

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

    return m,p,pi,y,y_bar,h,b, m._stopping_type
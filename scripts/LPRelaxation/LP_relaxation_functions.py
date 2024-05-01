from gurobipy.gurobipy import GRB
import model.BuildModel as bd
import gurobipy as gp
import time
# import scripts.DeniseMA.scripts.build_ean.read_entire_input as ri
# import scripts.DeniseMA.scripts.analyse_results.analyse_log as log
# from scripts.DeniseMA.scripts.analyse_results.evaluate_solutions_functions import *
# import scripts.DeniseMA.scripts.LPbased.LPmodel as lp
# import scripts.DeniseMA.scripts.model.BuildModel as bd
# import scripts.DeniseMA.scripts.build_ean.read_ean_functions as rd

# import scripts.DeniseMA.scripts.LPbased.LPmodel as lp

# import visualisations_main as vis
# import matplotlib.pyplot as plt
# import sucsessive_planning_functions as spf

# import scripts.DeniseMA.scripts.successive_sheafs.sort_alternatives as sort_alt
# import scripts.DeniseMA.scripts.successive_sheafs.successive_sheafs_functions as ssf
# import scripts.DeniseMA.scripts.visualisations.visualisations as vis
# import scripts.DeniseMA.scripts.utils.write_timetable as util
# #import successive_sheafs.successiveSheafs as sheafs
def LP_relaxation(modelname, ean, alternatives_dict, T, epsilon, zugfolge, curlyH, curlyS, filename,
                  h_type = 'continuous',b_type = 'continuous',
                  timeout = 60*30,
                 no_improvement_stop = False, feasibility_time_limit = 30, sol = {},
                  test_start = False, b_prio  = False,h_prio = False,
                  inequality = False):

    m = gp.Model(modelname)


    edges = [(i, j) for (i, j) in ean.edges] #inkl headway
    edges_woH = [(i, j) for (i, j) in ean.edges if ean[i][j]['type'] != 'headway']
    # set variables
    p = m.addVars(edges, name='p', vtype=GRB.BINARY, lb=0, ub=1) # upper bound 2 für IB formulation
    pi = m.addVars(ean.nodes(), name='pi', vtype=GRB.CONTINUOUS, lb=0, ub= T - 1)
    y = m.addVars(edges_woH, name='y', vtype=GRB.CONTINUOUS, lb=0)
    y_bar = m.addVars(edges_woH, name='y_bar', vtype=GRB.CONTINUOUS, lb=0)

    if h_type == 'integral':
        h = m.addVars(edges_woH, name='h', vtype=GRB.BINARY, lb=0, ub=1)
    else:
        h = m.addVars(edges_woH, name='h', vtype= GRB.CONTINUOUS, lb=0, ub=1)


    if b_type == 'integral':
        b = m.addVars(alternatives_dict.keys(), name='b', vtype=GRB.BINARY, lb=0, ub=1)
    else:
        b = m.addVars(alternatives_dict.keys(), name='b', vtype=GRB.CONTINUOUS, lb=0, ub=1)

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
                except:
                    continue

    m = bd.add_objective(m,h,y_bar,ean)
    m = bd.add_slack_assignment(m,p,pi,y,y_bar,h,ean,T)
    m = bd.add_PESP_constraints(m,p,pi,y,y_bar,h,ean,T)
    m = bd.arc_activation(m, ean, b, h, curlyS, alternatives_dict, relaxed = inequality)
    m = bd.sheaf_activation(m, ean, b, h, curlyS, alternatives_dict)
    m = bd.add_headway_constraints(m,p,pi,h,epsilon,zugfolge,T,curlyH)
    m = bd.fix_henkel(m,ean,pi)
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

    #filename = out_path+ modelname
    m.write(filename+'.lp')

    if timeout != False:
        m.setParam('TimeLimit', timeout)

    print('log file', filename)
    m.setParam('LogFile', filename +'.log')

    if b_prio:
        for F in alternatives_dict:
            b[F].BranchPriority = 9
    if h_prio:
        for (i,j) in edges_woH:
            h[(i,j)].BranchPriority = 9
    #m.setAttr("BranchPriority", h, [9]*len(h))

    m._cur_obj = float('inf')
    m._time = time.time()
    m._prev_obj = float('inf')

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

    # m._cur_obj = float('inf')
    # m._time = time.time()

    if no_improvement_stop:
        m.optimize(no_improvement_func)
    else:
        m.optimize()
    runtime = m.Runtime

    if m.status == GRB.INFEASIBLE:
        m.computeIIS()
        m.write(filename + "_infeasibility_info.ilp")
        return m, p, pi, y, y_bar, h, b
    m.printStats()

    try:
        m.write(filename+'.sol')
        all_vars = m.getVars()
        values = m.getAttr("X", all_vars)
        names = m.getAttr("VarName", all_vars)

    except:
        pass

    return m,p,pi,y,y_bar,h,b

def integer_measures(variable):
    integral = 0
    fractional = 0
    new_integral = 0
    for v in variable.values():
        # name = v.varName.strip('[')
        # name = name.strip(']')
        # name = int(name)
        # print(name)
        # print("{}: {}".format(v.varName, v.X))
        frac = v.X - int(v.X)

        if round(frac, 4) == 0:
            integral += 1
        else:
            fractional += 1

        new_integral += abs(v.X - 0.5)
    integral = integral / len(variable.values())
    fractional = fractional / len(variable.values())
    new_integral = new_integral/ len(variable.values())
    return integral, fractional, new_integral

def check_feasibility(modelname, ean, alternatives_dict, epsilon, zugfolge, curly_H,
                                               sheaf_dict, model_out_path,sol):
    m, p, pi, y, y_bar, h, b = LP_relaxation(modelname, ean, alternatives_dict, 200, epsilon, zugfolge, curly_H,
                                               sheaf_dict, model_out_path, feasibility_stop=True,
                                               feasibility_time_limit=2, sol=sol, test_start=True)
    if m.status == GRB.INFEASIBLE:
        return False
    else:
        print('correct solution')
        return True
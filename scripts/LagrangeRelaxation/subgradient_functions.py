# from scripts.DeniseMA.scripts.analyse_results.evaluate_solutions_functions import *
# import scripts.DeniseMA.scripts.LagrangeRelaxation.lagrange_relaxation_functions as lag
from utils.auswertung import *
import LagrangeRelaxation.lagrange_relaxation_functions as lag
import utils.analyse_log as log
import timeit
# import scripts.DeniseMA.scripts.analyse_results.evaluate_solutions_functions as ev
# import scripts.DeniseMA.scripts.model.BuildModel as bd
# import scripts.DeniseMA.scripts.build_ean.read_entire_input as ri



def subgradient(modelname, ean,ean_noH, alternatives_dict, T, epsilon,zugfolge, curly_H, sheaf_dict, filename,timeout,
               lambda_0,max_iterations,c_k,type_sheaf, type_activation, Z_star, timestamp, overall_timeout,model_out_path,
                c_k_dynamic = False,
                gap_stop = True,time_limit_after_callback = 20,
                time_out_per_iteration = 5*60,
                overall_time_out = 10 *60,
                hard_fix = True,
                hard_fix_relaxation_Ratio = 1,
                                start_sol = {}):
    lower_bounds = []
    norms = []
    sol = {}
    objective = 0
    step = 0
    old_sol = {}
    old_norm = float('inf')
    running_time = 0
    norm = float('inf')
    #k = 0
    hard_fix = {}
    additional_inequalities = []

    feasibility_time_limit =  10
    faulty_edges_forced = False
    for k in range(0, max_iterations):#100
        if norm <= 5:
            time_limit_after_callback = 30
        else:
            feasibility_time_limit = 30
        start = timeit.default_timer()
        # solve lagrangian
        model, p, pi, y, y_bar, h, b, L = lag.Lagrange_relaxation(modelname, ean, alternatives_dict, T, epsilon,
                                                                  zugfolge, curly_H, sheaf_dict, filename,
                                                                  lambda_0,
                                                                  sheaf_relaxation=type_sheaf,
                                                                  activation_relaxation=type_activation,
                                                                timeout = time_out_per_iteration,
                                                                  feasibility_stop=True,
                                                                  feasibility_time_limit= time_limit_after_callback ,
                                                                  gap_stop = gap_stop,
                                                                  sol= old_sol,
                                                                  test_start=False, prio=False,
                                                                  fixed = additional_inequalities,
                                                                  hard_fix = hard_fix)

        #timeout= timeout,

        sol_file = filename + '.sol'
        sol, objective = read_solution_file(sol_file)

        obj = model.getObjective()
        curr_objective = obj.getValue()
        lower_bounds.append(curr_objective)

        gap = model.MIPGap

        keys = []
        if type_sheaf:
            keys.extend([sheaf for sheaf in sheaf_dict])
        if type_activation:
            keys.extend([(i, j) for (i, j) in ean_noH.edges])

        # compute step size : classical approach
        norm = 0
        for index in range(len(L)):
            norm += abs(L[keys[index]].X)
        norms.append(round(norm,2))
        print('norm',round(norm,2))

        L_not0 = [keys[index] for index in range(len(L)) if L[keys[index]].X != 0]
        lambda_not0 = [keys[index] for index in range(len(lambda_0)) if lambda_0[keys[index]] != 0]

        penalty = 0
        for index in range(len(L)):
            (i,j) = keys[index]
            penalty += lambda_0[keys[index]] * L[keys[index]].X

        objective_wo_penalty = objective - penalty


        header = ['Model', 'iteration', 'len lambda', 'lambda not 0', 'len L', 'L not 0', 'norm','step','objective','gap',
                  'obj wo L', ' penalty', 'c_k']
        row = [modelname, k, len(lambda_0), len(lambda_not0), len(L), len(L_not0), norm, step, curr_objective,gap,
               objective_wo_penalty,penalty, c_k]

        results_file = model_out_path + modelname + '_multipliers_'+ timestamp + '.csv'
        log.write_detailed_results_excel(results_file, header, row, create_new_file=False)

        if model.SolCount <1:
            return 'no solution',-1, False, k+1

        hard_fix = {}
        additional_inequalities = []
        if norm == 0:
            #print('sol', sol['b'])
            print('objective', objective)
            # best solution found
            print('lower bounds: ', lower_bounds)
            return sol,objective, False,k+1


        else:

            if c_k_dynamic == True:
                if round(curr_objective) in [round(obj) for obj in lower_bounds[:-1]]:
                    print('change c_k')
                    c_k = 0.5*c_k

            step = c_k * (Z_star -curr_objective) / norm
            print('z*', Z_star, 'curr objective', curr_objective)

            for index in lambda_0:
                lambda_0[index] = max(0,lambda_0[index] + step * L[index].X)
                if norm == old_norm:
                    lambda_0[index]= lambda_0[index] + 10*step * L[index].X

                if L[index].X == 0 and lambda_0[index] != 0 :
                    additional_inequalities.append(index)

        stop = timeit.default_timer()
        running_time += (stop-start)
        old_sol = sol
        old_norm= norm

        k +=1


        table, time_out, objective, bound, gap, time, solution_count, solve_interrupted = log.evaluate_log(
            filename + '.log')
        if k >= max_iterations:
            abbruch = True
        else:
            abbruch=False

    print('lower bounds: ', lower_bounds)

    return sol, objective, abbruch,k

def no_solution_substitute(liste, penalty):
    for i, val in enumerate(liste):
        if val == '-':
            liste[i] = penalty
    return liste
def get_first_sol(log_dict):
    first_sol_index = -1
    first_sol_time = -1
    first_sol_obj = -1
    first_sol_gap = -1
    for i, time in enumerate(log_dict['Time']):
        if i == 0:
            if log_dict['Incumbent'][i] != -100:
                first_sol_index = i
            else:
                continue
        if log_dict['Incumbent'][i - 1] == -100 and log_dict['Incumbent'][i] != -100:
            # first solution found:
            first_sol_index = i
    if first_sol_index != -1:
        first_sol_time = log_dict['Time'][first_sol_index]
        first_sol_obj = log_dict['Incumbent'][first_sol_index]
        first_sol_gap = log_dict['Gap'][first_sol_index]

    return first_sol_index,first_sol_time,first_sol_obj,first_sol_gap

def get_first_occ_of_plateau_sol(log_dict, plateau_val):
    first_sol_index = -1
    first_sol_time = -1
    first_sol_obj = -1
    first_sol_gap = -1
    for i, time in enumerate(log_dict['Time']):
        if i == 0:
            if log_dict['Incumbent'][i] == plateau_val:
                first_sol_index = i
            else:
                continue
        if round(log_dict['Incumbent'][i - 1],3) != round(plateau_val,3)\
                and round(log_dict['Incumbent'][i],3) == round(plateau_val,3):
            # first solution found:
            first_sol_index = i

    if first_sol_index != -1:
        first_sol_time = log_dict['Time'][first_sol_index]
        first_sol_obj = log_dict['Incumbent'][first_sol_index]
        first_sol_gap = log_dict['Gap'][first_sol_index]

    return first_sol_index,first_sol_time,first_sol_obj,first_sol_gap

def get_sol_custom_time_cutoff(log_dict, custom_time):
    custom_time_cutoff_index = -1
    for i, time in enumerate(log_dict['Time']):
        if time > custom_time:
            custom_time_cutoff_index = i-1
            break
    sol_obj = log_dict['Incumbent'][custom_time_cutoff_index]
    sol_gap = log_dict['Gap'][custom_time_cutoff_index]

    return custom_time_cutoff_index, sol_obj, sol_gap

# open the file in the write mode
import csv
import pandas as pd
import matplotlib.pyplot as plt
import os
from pathlib import Path
import json
from collections import defaultdict
import pylab

def evaluate_log(gurobilogfile):
    size = {}
    solution_count = -10
    time_out = False
    presolved = False

    with open(gurobilogfile) as f:
        all_lines = f.readlines()
        # i= 0
        # while i == 0:
        #     print(f.next())
    #print(all_lines)
    table = []
    time_out = False
    objective = -100
    bound = -100
    gap = -100
    time = -100
    solution_count = False
    solve_interrupted = False
    sonderfall = False
    #print(all_lines)

    beginning_log = 0
    for line in all_lines[::-1]:
        #print(line)
        if 'logging started' in line:
            beginning_log = line
            all_lines = all_lines[all_lines.index(beginning_log):]
            break


    for index, line in enumerate(all_lines):
        if 'Explored 0 nodes' in line:
            print('sonderfall')
            sonderfall = True

        if "Nodes" in line and "Current Node" in line and "Objective Bounds" in line:
            #print(line)
            i = 3
            #print(all_lines[index+i])

            while index+i < len(all_lines) and all_lines[index+i] != '\n':
                #print(all_lines[index+i])

                table.append(all_lines[index+i])
                i += 1
            index = index + i

        if 'Solve interrupted' in line:
            solve_interrupted = True

        if 'Time limit reached' in line:
            time_out = True
        if ('Best objective' in line) and ('best bound' in line) and ('gap' in line):
            line = line.split(',')
            objective_part = line[0].strip()
            bound_part = line[1].strip()
            gap_part = line[2].strip()
            #print(objective_part)
            objective = as_number(objective_part.split(' ')[-1])
            bound = as_number(bound_part.split(' ')[-1])
            gap = gap_part.split(' ')[-1]
            gap = gap.strip('%')
            gap = as_number(gap.strip())


        if ('Explored' in line) and ('seconds') in line:
            #print(line)
            line = line.split(' ')
            for i,element in enumerate(line):
                if 'seconds' in element:
                    time = float(line[i-1])

        if 'Solution count' in line:
            line = line.split(':')
            solutions = line[0].split(' ')
            solution_count = solutions[-1]

    if sonderfall == True:
        table = ['0 \t 0 \t' + str(objective) + '\t 0 \t 0 \t' + str(objective)+'\t' + str(bound) +'\t' +str(gap) +'\t 0 \t' +str(time)]

    return  table, time_out, objective,bound,gap,time,solution_count, solve_interrupted


def as_number(entry):
    try:
        return round(float(entry),2)
    except:
        if '%' in entry:
            entry = entry.strip('%')
            return round(float(entry), 2)
        elif 's' == entry[-1]:
            entry = entry.strip('s')
            #print(entry)
            return round(float(entry), 2)
        else:
            return entry

def getfiles(dirpath):
    a = [s for s in os.listdir(dirpath)
         if os.path.isfile(os.path.join(dirpath, s))]
    a.sort(key=lambda s: os.path.getmtime(os.path.join(dirpath, s)))
    return a

def plot_log(log_dict, filename=""):
    all_values = [i for i in log_dict['Incumbent']]
    all_values.extend([i for i in log_dict['BestBd']])
    x = [i for i in range(len(log_dict['Incumbent']))]
    for val in log_dict['Incumbent']:
        if type(val) != float:
            print(val)
            print(type(val))
    # y = [0, 1, 2, 3, 4]
    tik = int((max(all_values) - min(all_values)) * 0.10)
    print('tik', tik)
    if tik <= 5:
        tik = 10

    y_pos = [i for i in range(int(min(all_values)), int(max(all_values)), tik)]
    # fig1, ax1 = plt.subplots()
    f, (ax1, ax2) = plt.subplots(1, 2, )
    ax1.set_yticks(y_pos)
    ax1.plot(x, log_dict['Incumbent'], label='Incumbent')
    ax1.plot([i for i in range(len(log_dict['BestBd']))], log_dict['BestBd'], label='Bestbd')

    yrange = max(all_values) - min(all_values)
    ax1.set_ylim(min(all_values) - yrange / 10, max(all_values) + yrange / 10)

    ax2.plot(x, log_dict['Gap'], label='Gap')
    plt.ylabel("Gap in %")
    print(log_dict['Gap'])
    # yrange = max(all_values) - min(all_values)
    # ax1.set_ylim(min(all_values) - yrange / 10, max(all_values) + yrange / 10)

    plt.title(filename)
    ax1.legend(loc='upper right')
    ax2.legend(loc='upper right')
    if filename != "":
        plt.savefig(filename, dpi=100, bbox_inches="tight")
        plt.close()
    else:
        plt.show()

    return

def create_log_dict(table, detailed = False):

    incumbent = []
    best_bound = []
    log_dict = {'Expl':[], 'Unexpl':[], 'Obj':[], 'Depth':[], 'IntInf' :[],'Incumbent':[],
                'BestBd':[], 'Gap':[], 'It / Node':[], 'Time':[]}
    keys = ['Expl', 'Unexpl', 'Obj', 'Depth', 'IntInf','Incumbent', 'BestBd', 'Gap', 'It / Node', 'Time']
    for l in table:
        #Nodes       | Current Node     | Objective Bounds         | Work
        #Expl Unexpl | Obj Depth IntInf | Incumbent BestBd Gap | It / Node Time

        #if 'Explored 0 nodes' in l:
        #print(l)

        line = l.split()
        if line[2] == 'infeasible':
            line.insert(4, '_')

        if line[2] == 'cutoff':
            line.insert(3, '_')

        if line[0] == 'H':
            line.insert(3, '_')
            line.insert(4, '_')

        elif 'H' in line[0]:
            line.insert(2, '_')
            line.insert(3, '_')
            line.insert(4, '_')

        if line[0] == '*':
            line.insert(2, '_')
        elif '*' in line[0]:
            line.insert(2, '_')
            line.insert(4, '_')

        for index,i in enumerate(line):
            #print('line',line)
            if detailed:
                log_dict[keys[index]].append(as_number(i))
            else:
                if i != '-' and i != '_':
                #print(line)
                    log_dict[keys[index]].append(as_number(i))
            #else:
            #    log_dict[keys[index]].append(log_dict[keys[index]][-1])
            #print(keys[index], as_number(i))
    return log_dict


def write_detailed_results_excel(file, header, row, create_new_file = False):
    #header = ['Model', 'Sortierung','#Linien', 'start/fixed','feasibility stop',
    #          'Linien','time','timeout','solution found','gap in %','objective']
    if os.path.isfile(file) and (create_new_file == False):
        with open(file, 'a', newline='') as f_object:
            writer_object = csv.writer(f_object, delimiter=';')
            writer_object.writerow(row)
            #f_object.write('\n')

            f_object.close()
    else:
        with open(file, 'w') as f_object:
            writer_object = csv.writer(f_object, delimiter=';')
            writer_object.writerow(header)
            writer_object.writerow(row)
            f_object.close()


def create_new_comparison_file(files, results_file, typ,append = False, config_file = []):

    total_time = 0
    for count,filename in enumerate(files):

        print(filename)
        table, time_out, objective, bound, gap, time, solution_count, solve_interrupted = evaluate_log(filename )
        log_dict = create_log_dict(table, detailed=True)
        print(log_dict.keys())
        incumbents = log_dict['Incumbent']

        total_time += time
        # get index of first solution
        first_solution_index = -1

        print('first_solution_index', first_solution_index)
        if typ == 'original':
            for i, val in enumerate(incumbents):
                if isinstance(val, float):
                    first_solution_index = i
                    break
            try:
                time_until_first_solution = log_dict['Time'][first_solution_index]
            except:
                time_until_first_solution = 'problem'
        else:

            try:

                for i, val in enumerate(incumbents):


                    if isinstance(val, float) and val < config_file['penalty']:
                        first_solution_index = i
                        break
                time_until_first_solution = log_dict['Time'][first_solution_index]
                print(time_until_first_solution)
            except:
                time_until_first_solution = 'problem'



        path = filename.split('/')
        filename_short = path[-1]
        date = path[-2]
        type = typ
        modelname = filename_short

        print(path)
        header = ['szenario','model', 'typ', 'date', 'comment']
        if typ != 'original':
            szenario = modelname[:modelname.rfind('_curr_')]
        else:
            szenario = modelname[:modelname.rfind('.log')]

        row = [szenario,modelname, type, date, '']
        if config_file:
            row.extend(list(config_file.values()))
            header.extend(list(config_file.keys()))
        else:
            row.extend([None for i in range(10)])

        row.extend([time, time_out, solution_count, time_until_first_solution, gap, objective])
        header.extend(['time', 'timeout', 'solution found', 'time 1. solution','gap in %', 'objective'])

        if count == 0 and (append == False):
            #print('if')
            write_detailed_results_excel(results_file, header, row, create_new_file=True)
        else:
            write_detailed_results_excel(results_file, header, row, create_new_file=False)
    if typ != 'original':
        row = ['' for i in header]
        row[0] = szenario
        row[1] = 'complete'
        row[-6] = total_time
        row[-7] = 'total time'
        write_detailed_results_excel(results_file, header, row, create_new_file=False)
        #print(time_out, objective, bound, gap, time, solution_count, solve_interrupted )
        #print(table)
    return



def get_sortierung(sortierung_file):
    with open(sortierung_file) as f:
        lines = f.readlines()

    # letzte iteration/sheaf = vollständiges modell
    sortierung = []
    for line in lines:
        if 'sortierung' in line:
            continue
        else:
            line = line.strip('\n')
            line = line.strip('[')
            line = line.strip(']')
            line = line.split(',')
            #print(line)
            try:
                sortierung.append([int(i) for i in line])
            except:
                sortierung.append([])

    return sortierung

def comparison_one_run(all_models, date, results_file, typ, additional = False):
    for count,model in enumerate(all_models):
        model_path = path + model + '/' + typ + '/run_'+ date +'/'
        # read config file
        if typ != 'original':
            print(model_path+model+'_configurations.txt')
            config_file = json.load(open(model_path+model+'_configurations.txt'))
            sortierung = get_sortierung(model_path + model + '_sheaf_sortierung.txt')
        else:
            filename = model_path + model +'.log'
            files = [filename]
            if (count == 0) and (additional == False):
                create_new_comparison_file(files, results_file, typ, append=False, config_file=[])
            else:
                create_new_comparison_file(files, results_file, typ, append=True, config_file=[])
            continue
        # read sheaf sortierung

        print(sortierung)
        files = []
        for sheafs in sortierung:
            filename = model_path + model + '_curr_' + str(sheafs) + '.log'
            files.append(filename)
        if (count == 0) and (additional == False):
            create_new_comparison_file(files, results_file, typ, append=False, config_file=config_file)
        else:
            create_new_comparison_file(files, results_file, typ, append=True, config_file=config_file)
    return


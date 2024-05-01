import sys
from collections import defaultdict
import yaml
import os
directory = os.getcwd()
print(directory)
script_directory = os.path.dirname(os.path.realpath(__file__))
print(script_directory)
config = yaml.safe_load(open(script_directory + '/param.yaml')) #' ../param.yaml'
#config = yaml.safe_load(open(sys.argv[-1]))

zugfolge = config['PESP']['zugfolge']
epsilon = config['PESP']['epsilon']
T = config['PESP']['T']
path = config['paths']['in_path']
out_path = config['paths']['out_path']
all_models = config['instances']
custom_time = config['Auswertungszeitpunkt']

# stuff for main
if config['main']['chosen']:
    timeout = config['main']['timeout']
    feasibility_stop = config['main']['feasibility_stop']
    feasibility_time_limit = config['main']['feasibility_timelimit']
    results_file = config['main']['results_file']


# stuff for RENS
if config['RENS']['chosen']:
    timeout = config['RENS']['timeout']
    feasibility_stop = config['RENS']['feasibility_stop']
    feasibility_time_limit = config['RENS']['feasibility_timelimit']
    if config['RENS']['relaxed']:
        results_file = config['RENS']['results_file_relaxed']
    else:
        results_file = config['RENS']['results_file']
    fixed_integer_ratio = config['RENS']['fixed_integer_ratio']
    ratios_relax = config['RENS']['ratios_relax']
    path = config['RENS']['in_path']
    out_path = config['RENS']['out_path']

# stuff for RENS

if config['RINS']['chosen']:
    timeout = config['RINS']['timeout']
    feasibility_stop = config['RINS']['feasibility_stop']
    feasibility_time_limit = config['RINS']['feasibility_timelimit']
    rins_relax = config['RINS']['relaxed']
    if config['RINS']['relaxed']:
        results_file = config['RINS']['results_file_relaxed']
    else:
        results_file = config['RINS']['results_file']
    rins_epsilon = config['RINS']['epsilon']
    ratios_relax = config['RINS']['ratios_relax']
    path = config['RINS']['in_path']
    out_path = config['RINS']['out_path']


if config['Lagrange']['chosen']:
    timeout = config['Lagrange']['timeout']
    feasibility_stop = config['Lagrange']['feasibility_stop']
    feasibility_time_limit = config['Lagrange']['feasibility_timelimit']
    results_file = config['Lagrange']['results_file']
    max_iter = config['Lagrange']['max_iterations']
    c_k = config['Lagrange']['c_k']
    type_sheaf = config['Lagrange']['type_sheaf']
    type_activation = config['Lagrange']['type_activation']
    path = config['Lagrange']['in_path']
    out_path = config['Lagrange']['out_path']
    overall_timeout = config['Lagrange']['overall_timeout']

if config['Branching']['chosen']:
    timeout = config['Branching']['timeout']
    feasibility_stop = config['Branching']['feasibility_stop']
    feasibility_time_limit = config['Branching']['feasibility_timelimit']
    results_file = config['Branching']['results_file']
    max_iter = config['Branching']['max_iterations']
    path = config['Branching']['in_path']
    out_path = config['Branching']['out_path']



def write_config(filename):
    filename =  filename + '.yaml'
    with open(filename, "w") as file_object:
        yaml.dump(config, file_object)
    return

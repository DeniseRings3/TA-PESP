import sys
from collections import defaultdict
import yaml
import os
directory = os.getcwd()
print(directory)
script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
print(script_directory)
config = yaml.safe_load(open(script_directory+'/param.yaml'))
#config = yaml.safe_load(open(sys.argv[-1]))

zugfolge = config['PESP']['zugfolge']
epsilon = config['PESP']['epsilon']
T = config['PESP']['T']
path = config['paths']['in_path']
out_path = config['paths']['out_path']
all_models = config['instances']

color_dict = config['color dict']
bar_plot_dict = config['bar_plot']
line_plot_dict = config['line_plot']

path_dict = {}
path_dict['main'] = {'results_file':config['main']['results_file'],
                       'path':config['main']['path']}
path_dict['RENS'] = {'results_file':config['RENS']['results_file'],
'path':config['RENS']['path']}

path_dict['RENS relaxed'] = {'results_file':config['RENS relaxed']['results_file'],
                       'path':config['RENS relaxed']['path']}

path_dict['RINS relaxed'] = {'results_file':config['RINS relaxed']['results_file'],
                       'path':config['RINS relaxed']['path']}
path_dict['Lagrange'] = {'results_file':config['Lagrange']['results_file'],
                       'path':config['Lagrange']['path']}

path_dict['branching'] = {'results_file':config['branching']['results_file'],
                       'path':config['branching']['path']}

print('param geladen')
def write_config(filename):
    filename =  filename + '.yaml'
    with open(filename, "w") as file_object:
        yaml.dump(config, file_object)
    return



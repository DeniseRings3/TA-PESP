import yaml
import os
# Create an empty dictionary

config_dict=dict()
# Add configuration data to the dictionary
config_dict["PESP"]={'zugfolge': 25, 'epsilon': 17, 'T':200}
config_dict['paths']={'in_path': '../../../processed/',  #'../../../../processed/'
                      'out_path': '../processed/'} #'../../processed/'

config_dict['instances'] = ['BBER_BBU','BBKS_BWT','BBOS_BWIN_BTG', 'BGAS_BKW',
                            'BNB_BSNH_BSAL_BPHD','BBUP_O','BBUP_W',
                          'BPKW_BKRW_BSNF_O','BWKS_medium_september','BGB_BWES']

config_dict['Auswertungszeitpunkt'] = 10*60

config_dict['main'] = {'chosen': False,
                       'timeout': 3*60*60,# * 60
                       'feasibility_stop':False,
                       'feasibility_timelimit': 20*60,
                       'results_file':'results_file_main_equality_2703.csv',
                       'path': '../../processed/' + '/original/'}

config_dict['RENS'] = {'chosen':False,
                       'timeout': 60 * 60,
                       'feasibility_stop':False,
                       'feasibility_timelimit':1,
                       'fixed_integer_ratio': 0.4,
                       'results_file':'results_file_RENS_ineq_0504.csv',
                       'relaxed':True,
                       'results_file_relaxed':'results_file_RENS_relaxed_ineq2803',
                       'ratios_relax': [0.9,0.6],#,0.8,0.6
                       'in_path':'../../processed/',
                       'out_path':'../processed/',
                       'path':['../../processed/','/RENS/']}

config_dict['RINS'] = {'chosen': False,
                       'timeout': 30 * 60,
                       'feasibility_stop':False,
                       'feasibility_timelimit':1,
                       'epsilon': 0.01,
                       'results_file':'results_file_RINS_ineq.csv',
                       'relaxed': True,
                       'results_file_relaxed':'results_file_RINS_relaxed_random_0504.csv',
                       'ratios_relax': [0.9, 0.6],
                        'in_path':'../../../../processed/',
                       'out_path':'../../processed/',
                        'path':['../../processed/','/RINS/']}

config_dict['Lagrange'] = {'chosen': False,
                       'timeout': 1 * 60,
                       'feasibility_stop':False,
                       'feasibility_timelimit':1,
                       'results_file': 'results_lagrange_2903.csv',
                        'max_iterations' : 10,
                        'c_k': 2,
                        'type_sheaf' : False,
                        'type_activation' : True,
                        'in_path':'../../../processed/',
                       'out_path':'../processed/',
                        'path':['../../processed/','/Lagrange/'],
                           'overall_timeout':10*60}

config_dict['Branching'] = {'chosen': True,
                       'timeout': 60 * 60,
                       'feasibility_stop':False,
                       'feasibility_timelimit':1,
                       'results_file': 'results_branching_improvement_random_29_04.csv',
                        'max_iterations' : 10,
                        'in_path':'../../../../processed/',
                       'out_path':'../processed/',
                        'path':['../processed/','/Branching/']}

# Save the dictionary to a YAML file
script_directory = os.path.dirname(os.path.realpath(__file__))
with open(script_directory+"/param.yaml","w") as file_object:
    yaml.dump(config_dict,file_object)



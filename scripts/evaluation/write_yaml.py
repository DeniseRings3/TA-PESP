import yaml
# Create an empty dictionary
config_dict=dict()

# Add configuration data to the dictionary
config_dict["PESP"]={'zugfolge': 25, 'epsilon': 17, 'T':200}
config_dict['paths']={'in_path': '../../../../processed/',
                      'out_path': '../../processed/'}
config_dict['instances'] = ['BBER_BBU','BBKS_BWT','BBOS_BWIN_BTG', 'BGAS_BKW','BGB_BWES',
                            'BNB_BSNH_BSAL_BPHD', 'BBUP_O','BBUP_W',
              'BPKW_BKRW_BSNF_O', 'BWKS_medium_september']

#'BBKS_BWT','BBOS_BWIN_BTG', 'BGAS_BKW','BGB_BWES', 'BNB_BSNH_BSAL_BPHD', 'BBUP_O','BBUP_W'
#              'BPKW_BKRW_BSNF_0', 'BWKS_medium_september']

config_dict['main'] = {'results_file':'results_file_main.csv',
                       'path': ['../../processed/','/original/']}

config_dict['RENS'] = {'results_file':'results_file_RENS.csv',
                       'path': ['../../processed/','/RENS/']}
config_dict['RENS relaxed'] = {'results_file':'results_file_RENS_relaxed.csv',
                        'path': ['../../processed/','/RENS/']}
config_dict['RINS relaxed'] = {'results_file':'results_file_RINS_relaxed.csv',
                       'path': ['../../processed/','/RINS/']}
config_dict['Lagrange'] = {'results_file':'results_lagrange_act_sheaf.csv',
                       'path': ['../../processed/','/original/LP_based/']}

config_dict['branching'] = {'results_file':'results_branching.csv',
                       'path': ['../../processed/','/Branching/']}

config_dict['color dict'] = {'main': 'tab:blue',
                             'RENS': 'tab:orange',
                             'RENS relaxed': 'sandybrown',
                            'branching': 'tab:cyan',
                             'RINS':'tab:green',
                             'Lagrange act':'indianred',
                             'Lagrange act sheaf':'firebrick',
                             'RENS relaxed only_opt': 'sandybrown',
                            'RENS relaxed random': 'sienna',
                             'RENS relaxed other alternatives': 'peru',
                             'RENS relaxed slack': 'chocolate',

                           'RINS relaxed custom': 'forestgreen',
                            'RINS relaxed random': 'limegreen',
                             'RINS relaxed other alternatives': 'darkgreen',
                             'RINS relaxed slack': 'palegreen'
                             }

config_dict['bar_plot'] = {'cut-off': 60*60}
config_dict['line_plot'] = {'cut-off': 60*60}

# Save the dictionary to a YAML file
with open("param.yaml","w") as file_object:
    yaml.dump(config_dict,file_object)

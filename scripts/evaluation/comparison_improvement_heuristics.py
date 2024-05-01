import math
import statistics
from collections import defaultdict
import scripts.DeniseMA.scripts.utils.auswertung as util
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.ticker import MaxNLocator
import matplotlib.colors as mcolors
import os
import scripts.DeniseMA.scripts.analyse_results.analyse_log as log
def no_solution_substitute(liste, penalty):
    for i, val in enumerate(liste):
        if val == '-':
            liste[i] = penalty
    return liste

color_dict = {'main' : 'tab:blue',
            'RINS': 'tab:orange',
            '(0.9,sheaf)':'peru',
            '(0.9,slack)':'chocolate',
            '(0.9,random best)':'sandybrown',
            '(0.9,random worst)': 'burlywood',
            ''
            '(0.6,sheaf)':'limegreen',
            '(0.6,slack)':'darkgreen',
            '(0.6,random best)': 'palegreen',
            '(0.6,random worst)':'forestgreen',

            '(branching,sheaf)':'palevioletred',
            '(branching,slack)':'mediumvioletred',
            '(branching,random best)': 'lightpink',
            '(branching,random worst)':'plum',

              }

file = r'/Users/deniserings/Documents/zib/s-bahn-data/scripts/DeniseMA/processed/final/start_heuristics_first_sol_time.xlsx'
path = r'/Users/deniserings/Documents/zib/s-bahn-data/scripts/DeniseMA/processed/final/'
df = pd.read_excel(file)
df.set_index('Model',inplace=True)

all_models =  [#'BPKW_BKRW_BSNF_O',
                'BWKS_medium_september',
               'BBKS_BWT',
             #'BBUP_W','BBUP_O',
           #   'BNB_BSNH_BSAL_BPHD','BGB_BWES'#,
    ]

#'BBER_BBU', 'BGAS_BKW',    'BBOS_BWIN_BTG',
paths = {'main': ['original_with_start_sol/', '_start_sol.log'],
         'RINS': ['RINS/standard/','_no relaxation_1.log'],
         '(0.9,sheaf)': ['RINS/relaxed/','_other alternatives_0.9.log'],
         '(0.9,slack)': ['RINS/relaxed/','_slack_0.9.log'],
         '(0.9,random best)': ['RINS/random/','_0.9.log'],
         '(0.9,random worst)': ['RINS/random/','_0.9.log'],

         '(0.6,sheaf)':['RINS/relaxed/','_other alternatives_0.6.log'],
         '(0.6,slack)': ['RINS/relaxed/','_slack_0.6.log'],
        '(0.6,random best)': ['RINS/random/','_0.6.log'],
         '(0.6,random worst)': ['RINS/random/','_0.6.log'],
         '(branching,sheaf)' : ['RapidBranching/standard/','_other alternatives_'],
        '(branching,slack)' : ['RapidBranching/standard/','_slack_'],
        '(branching,random best)' : ['RapidBranching/random/','.log'],
        '(branching,random worst)' : ['RapidBranching/random/','.log']
         }

heuristics = ['main','RINS',
               '(0.9,sheaf)','(0.9,slack)', '(0.9,random best)','(0.9,random worst)',
               '(0.6,sheaf)', '(0.6,slack)', '(0.6,random best)', '(0.6,random worst)',
               '(branching,sheaf)', '(branching,slack)',
              '(branching,random best)','(branching,random worst)']
heuristics_short = ['main','RINS',
               '0.9 sheaf',' 0.9 slack', '0.9 rb','0.9,rw',
               '0.6 sheaf', '0.6 slack', '0.6 rb', '0.6,rw',
               'branching sheaf', 'branching slack',
              'branching rb','branching rw']



results_file_branching = r'/Users/deniserings/Documents/zib/s-bahn-data/scripts/DeniseMA/processed/final/RapidBranching/standard/results_branching_improvement_2904.csv'
results_branching = pd.read_csv(results_file_branching,delimiter=';')
results_branching.set_index('Model',inplace=True)
df_dict_standard = {g: d for g, d in results_branching.groupby('type')}

results_file_branching_random = r'/Users/deniserings/Documents/zib/s-bahn-data/scripts/DeniseMA/processed/final/RapidBranching/random/results_branching_improvement_random_0704.csv'
results_branching_random = pd.read_csv(results_file_branching_random,delimiter=';')

df_dict_random = {g: d for g, d in results_branching_random.groupby('Model')}

for model in df_dict_random:
    df_dict_random[model].set_index('type', inplace=True)
    print(model,df_dict_random[model])
print('df_dict random',df_dict_random)



figure_title = 'Improvement Heuristics - Objective Function'

plot_dict = defaultdict(lambda:defaultdict(lambda:[]))

best_worst_dict = defaultdict(lambda:defaultdict(lambda:[]))


for modelname in all_models:
    for version in heuristics:
        print('modelname',modelname, 'version',version)
        dir = path + paths[version][0] + modelname + '/'

        if 'best' in version:
            dir = path + paths[version][0] + modelname + '/best/'
        elif 'worst' in version:
            dir = path + paths[version][0] + modelname + '/worst/'
        #print(dir)
        try:
            files = os.listdir(dir)
        except:
            print('problem')
            continue

        for file in files:
            #print(file)
            #print(paths[version][1] )

            if paths[version][1] in file and ('test' not in file) and ('log' in file) :
                logfile = file
                print('logfile', logfile)
                if ('branching' in version) and ('random' in version):
                    parts = logfile.split('_')
                    for i,part in enumerate(parts):
                        if 'subMBP' in part:
                            number = parts[i-1]
                    if 'best' in version:
                        best_worst_dict[modelname]['best'] = number
                    else:
                        best_worst_dict[modelname]['worst'] = number


                table, time_out, objective, bound, gap, time, solution_count, solve_interrupted = log.evaluate_log(dir + logfile)
                print('solution count',modelname,version,solution_count)
                if int(solution_count) >=0:
                    temp_log_dict = log.create_log_dict(table, detailed=True)
                    print(modelname,'version', version)



                    temp_log_dict['Incumbent'] = no_solution_substitute(temp_log_dict['Incumbent'], -100)
                    first_sol_index, first_sol_time, first_sol_obj, first_sol_gap = util.get_first_sol(temp_log_dict)
                    plat_index, plat_time, plat_obj, plat_gap = util.get_first_occ_of_plateau_sol(temp_log_dict,
                                                                                                  temp_log_dict[
                                                                                                      'Incumbent'][
                                                                                                      -1])

                    print(temp_log_dict['Incumbent'])
                    print('plateau index', plat_index)
                    print('length', len(temp_log_dict['Incumbent']))


                    if '_september' in modelname:
                        plat_time = min(plat_time,600)
                        plat_index, plat_time, plat_obj, plat_gap = util.get_first_occ_of_plateau_sol(temp_log_dict,8771.00000)

                    for key in temp_log_dict:
                        end = min([plat_index +10, len(temp_log_dict[key])])
                        temp_log_dict[key] = temp_log_dict[key][first_sol_index: end]


                    if 'branching' in version:
                        # add time of previous iterations
                        if 'random' in version:

                            # get random number
                            if 'best' in version:
                                random_number = best_worst_dict[modelname]['best']
                            else:
                                random_number = best_worst_dict[modelname]['worst']

                            #df_dict_random[modelname].set_index('type', inplace=True)
                            print('version in if', version)
                            print(df_dict_random[modelname])
                            prev_time = df_dict_random[modelname].loc[random_number, 'prev time']



                        else:
                            df_dict = df_dict_standard

                            if 'slack' in version:
                                prev_time = df_dict['slack'].loc[modelname,'prev time']
                            else:
                                prev_time = df_dict['other alternatives'].loc[modelname,'prev time']

                        for index,time in enumerate(temp_log_dict['Time']):
                            temp_log_dict['Time'][index] += prev_time


                    plot_dict[modelname][version] = temp_log_dict
                    print('plot dict',modelname,version)
                    print(plot_dict[modelname][version] )





fig, ax = plt.subplots(math.ceil(len(all_models) / 1)+1, 1,squeeze=False)
plt.subplots_adjust(hspace=0.75, wspace=0.3)
#fig.suptitle(figure_title, fontsize=14, weight='bold')

column = 'Incumbent'

for counter, modelname in enumerate(all_models):

    print('modelname')
    print(modelname)
    print(plot_dict[modelname].keys())
    i = counter #  // 2
    j = 0#counter #% 2

    all_vals = []
    for version in plot_dict[modelname].keys():

        all_vals.extend(plot_dict[modelname][version][column])

        ax[i,j].plot(plot_dict[modelname][version]['Time'],plot_dict[modelname][version][column],
                 color = color_dict[version], label = version)

    plt.sca(ax[i, j])
    plt.xticks(fontsize = 12)
    plt.yticks(fontsize=12)
    if 'september' in modelname:
        plt.xlim(0,200)

    plt.title(modelname,fontsize =14)
    ax[i, j].xaxis.set_major_locator(MaxNLocator(integer=True))
    ax[i, j].set_ylabel("objective",  labelpad=10,fontsize=14)
    ax[i, j].set_xlabel("time in sec",fontsize=14)

plt.sca(ax[-1, -1])
handles = [plt.Rectangle((0,0),1,1, color=color_dict[label]) for label in heuristics]
plt.legend(handles, heuristics_short, loc='center', bbox_to_anchor=(0.5, 1), ncol=7, fontsize='12')
plt.axis('off')
filename = path + column + '.png'

path = r'/Users/deniserings/Documents/zib/s-bahn-data/scripts/DeniseMA/processed/final/images/'

mng = plt.get_current_fig_manager()
mng.full_screen_toggle()

plt.tight_layout() # to fit everything in the prescribed area
#plt.show()
fig.savefig(path+'improvement_objective.jpg', dpi=1200) #, format='eps',
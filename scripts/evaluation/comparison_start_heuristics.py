import math
import statistics
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.ticker import MaxNLocator
from pylab import *
from tikzplotlib import save as tikz_save
import matplotlib.colors as mcolors

file = r'/Users/deniserings/Documents/zib/s-bahn-data/scripts/DeniseMA/processed/final/start_heuristics_first_sol_objective.xlsx'

df = pd.read_excel(file)
df.set_index('Model',inplace=True)
all_models =  [
    #'BBER_BBU', 'BGAS_BKW',
           'BPKW_BKRW_BSNF_O','BBOS_BWIN_BTG',
        'BWKS_medium_september', 'BBKS_BWT',
          'BBUP_W','BBUP_O',
            'BNB_BSNH_BSAL_BPHD','BGB_BWES'
    ]


print(df.head())


subtitle = ['inequality',
            'RENS',
            '(0.9,alternatives)',
            '(0.9,slack)',
            '(0.9,random best)',
            '(0.9,random worst)',
            '(0.6,alternatives)',
            '(0.6,slack)',
            '(0.6,random best)',
            '(0.6,random worst)',
            '(Lagrange,feasibility stop)',
            '(Lagrange,gap stop)']

display_subtitle = ['ineq',
            'RENS',
            'sheaf \n 0.9',
            'slack \n 0.9',
            'rb\n 0.9',
            'rw \n 0.9',
            'sheaf \n 0.6',
            'slack \n 0.6',
            'rb \n 0.6',
            'rw \n 0.6',
            'Lag\n feas ',
            'Lag \n gap']

color_dict = {'inequality' : 'tab:blue',
            'RENS': 'tab:orange',
            '(0.9,alternatives)':'peru',
            '(0.9,slack)':'chocolate',
            '(0.9,random best)':'sandybrown',
            '(0.9,random worst)': 'burlywood',
            ''
            '(0.6,alternatives)':'lightgreen',
            '(0.6,slack)':'limegreen',
            '(0.6,random best)': 'palegreen',
            '(0.6,random worst)':'forestgreen',

            '(Lagrange,feasibility stop)':'lightcoral',
            '(Lagrange,gap stop)':'indianred'
              }
    

fig, ax = plt.subplots(math.ceil(len(all_models)/2), 2,squeeze=False)#,,sharey='row'

plt.subplots_adjust(wspace=0.05)


for counter,modelname in enumerate(all_models):

    print('modelname')
    print(modelname)
    i = counter // 2
    j = counter % 2


    bar_plot_vals = []
    labels = []
    colors = []

    bar_plot_labels = []
    for version in subtitle:


        if df.at[modelname,version] == 0:
            ratio = 0
            bar_plot_vals.append(ratio)
            labels.append(str(0))
            colors.append(color_dict[version])

        elif  df.at[modelname,version] == -1 or df.at[modelname,version] == '-' :
            ratio = 0
            bar_plot_vals.append(ratio)
            labels.append('-')
            colors.append(color_dict[version])

        elif df.at[modelname,'inequality'] == 0 and df.at[modelname,version] != 0:
            ratio = df.at[modelname,version]
            print(ratio)
            bar_plot_vals.append(float(ratio))
            labels.append(str(round(ratio,2)))
            colors.append(color_dict[version])

        else:

            ratio =  df.at[modelname,version] / df.at[modelname,'inequality']

            print(ratio)
            bar_plot_vals.append(ratio)
            labels.append(round(ratio,2))
            colors.append(color_dict[version])

    bar_plot_x = [i for i in range(len(labels))]

    maximum = max([i for i in bar_plot_vals if i <= 5])
    for c,val in enumerate(bar_plot_vals):
        if val > 5 and maximum >0:
            bar_plot_vals[c] = maximum + bar_plot_vals[c] /maximum

    ax[i,j].bar(bar_plot_x, bar_plot_vals,  color= colors, alpha=1)

    ax[i,j].xaxis.set_major_locator(MaxNLocator(integer=True))


    pos = [i for i in range(len(labels))]
    if i == len(all_models)/2-1:
        ax[i,j].set_xticks(pos, display_subtitle, rotation='horizontal', fontsize = 12)
    else:
        ax[i,j].xaxis.set_tick_params(labelbottom=False)

    plt.sca(ax[i,j])
    y_min = min(bar_plot_vals)
    y_max = max(bar_plot_vals)
    plt.ylim(0.7, 1.1)


    plt.title(modelname, fontsize = 14,)

    for index,version in enumerate(labels):

        height = 1#*max(bar_plot_vals)/2

        plt.text(bar_plot_x[index], height, labels[index], horizontalalignment='center', color='black',
        fontsize = 12, weight='bold') #           weight='bold'

    plt.axhline(y=1, linewidth=1.5, color='k',linestyle = '--')


labels = list(color_dict.keys())
handles = [plt.Rectangle((0,0),1,1, color=color_dict[label]) for label in labels]


path = r'/Users/deniserings/Documents/zib/s-bahn-data/scripts/DeniseMA/processed/final/images/'

mng = plt.get_current_fig_manager()
mng.full_screen_toggle()

plt.tight_layout() # to fit everything in the prescribed area
#plt.show()
fig.savefig(path+'first_sol_objective.jpg', dpi=1200)

import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.ticker import MaxNLocator
import matplotlib.colors as mcolors

file = r'/Users/deniserings/Documents/zib/s-bahn-data/scripts/DeniseMA/processed/final/ComparisonEqualityInequality.xlsx'

df = pd.read_excel(file)
all_models =  ['BBER_BBU', 'BGAS_BKW',
            'BPKW_BKRW_BSNF_O',
               'BBOS_BWIN_BTG',
               'BWKS_medium_september',
            'BBKS_BWT',
             'BBUP_W','BBUP_O',
                        'BNB_BSNH_BSAL_BPHD','BGB_BWES']
print(df.head())
df_dict = {g: d for g, d in df.groupby('Constraint')}
df_dict['inequality'].set_index('modelname',inplace=True)

df_dict['equality'].set_index('modelname',inplace=True)
print(df_dict.keys())


# fig, ax = plt.subplots(2, 2)
# plt.subplots_adjust(hspace=0.75, wspace=0.3)
# fig.suptitle(figure_title, fontsize=14, weight='bold')

subtitle = ['First Solution (Time)',
            'First Solution (Objective)',
            'Final Solution (Time)',
            'Final Solution (Objective)']
display_subtitle = ['First Solution - Time',
                    'First Solution - Objective',
                    'Plateau Solution - Time',
                    'Plateau Solution - Objective']

for counter,version in enumerate(subtitle):
    #figure_title = 'Comparison of Inequality and Equality Formulation'

    print('version')
    print(version)
    i = counter // 2
    j = counter % 2

    all_vals = []
    print(version)
    bar_plot_x = [i for i in range(len(all_models))]
    bar_plot_vals = []
    colors = []
    labels = []
    for model in all_models:
        df_ineq = df_dict['inequality']
        df_eq = df_dict['equality']
        if df_ineq.at[model,version] == 0 or df_eq.at[model,version] == 0 :
            ratio = 0

        else:
            try:
                ratio = df_ineq.at[model,version] /df_eq.at[model,version]
            except:
                 ratio = 0
        print('ineq', df_ineq.at[model,version], 'eq',df_eq.at[model,version])
        print('ratio',ratio)
        labels.append(str(round(ratio, 2)))
        # scale first solution for BNB_BSNH_BSAL_BPHD
        #if model  == 'BNB_BSNH_BSAL_BPHD' and version == 'First Solution (Time)':
       #     ratio = ratio/10

        bar_plot_vals.append(ratio)

        if round(ratio,2) < 1:
            colors.append('tab:green')
        elif round(ratio,2) == 1:
            colors.append('tab:blue')

        else:
            colors.append('tab:red')


    plt.bar(bar_plot_x, bar_plot_vals, color=colors, alpha=0.5)

    y_min = min(bar_plot_vals)
    y_max = max(bar_plot_vals)
    print('ymin',y_min,'ymas',y_max)
    #plt.xaxis.set_major_locator(MaxNLocator(integer=True))

    if version == 'Final Solution (Objective)':
        plt.ylim(y_min - 0.01 * y_min, y_max + 0.01 * y_max)
        lowest_pos = max([0,y_min -0.5* 0.01])
    else:
        plt.ylim(y_min - 0.05 * y_min, y_max + 0.05 * y_max)
        lowest_pos = max([0,y_min - 0.5* 0.05])
    #plt.xlim(0, 10)
    pos = [i for i in range(0,len(all_models))]
    x_labels = [i for i in range(1,len(all_models)+1)]
    plt.xticks(pos, x_labels, rotation='horizontal', fontsize=18)
    plt.yticks(fontsize=18)

    # if i == 0 and j == 0:
    #     pos = [i for i in range(0,3)]
    #     pos.append(6)
    #y_labels = [i for i in pos]
    #     y_labels[-1] = 60
    #plt.yticks(pos, y_labels, rotation='horizontal', fontsize=18)


    plt.title(display_subtitle[counter], fontsize=12, weight='bold')
    plt.ylabel('inequ/equ ratio',fontsize=18, weight='bold')
    plt.xlabel('scenarios',fontsize=18, weight='bold')
    print(labels)
    for index, model in enumerate(all_models):
        plt.text(bar_plot_x[index], lowest_pos,labels[index], horizontalalignment='center', color='black',
                 weight='bold', fontsize=18)

#plt.sca(ax[0, 0])
#plt.legend( loc='upper center', bbox_to_anchor=(0.5, 1.2), ncol=3, fontsize='8')
#filename = out_path + column + '.png'
#plt.savefig(filename, dpi=600)
    plt.show()
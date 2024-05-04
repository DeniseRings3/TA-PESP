import math
from collections import defaultdict
import build_ean.read_ean_functions as rd
from matplotlib.ticker import MaxNLocator
import build_ean.read_entire_input as ri
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import csv
# Configurations
#  move this to config file
#######################################################################################################################
zugfolge = 25
epsilon = 17
T = 200
timeout = 180*60

path = r'/Users/deniserings/Documents/zib/s-bahn-data/processed/'
#path = r'/data/optimi/optimi/kombadon/drings/SBahn/s-bahn-data/processed/'
#out_path = r'/data/optimi/optimi/kombadon/drings/SBahn/s-bahn-data/scripts/DeniseMA/'
out_path = r'/Users/deniserings/Documents/zib/s-bahn-data/scripts/DeniseMA/'

results_file = out_path + 'processed/results_master_file.csv'

#######################################################################################################################

all_models = ['BBER_BBU', 'BGAS_BKW',
            'BPKW_BKRW_BSNF_O',
               'BBOS_BWIN_BTG',
                'BWKS_medium_september',
               'BBKS_BWT',
             'BBUP_W','BBUP_O',
              'BNB_BSNH_BSAL_BPHD','BGB_BWES']
    #['BBER_BBU','BBKS_BWT','BBOS_BWIN_BTG', 'BGAS_BKW','BGB_BWES', 'BNB_BSNH_BSAL_BPHD']
new_models = ['BBER_BBU','BBUP_O','BBUP_W',
              'BPKW_BKRW_BSNF_O', 'BWKS_medium_september']



fig, ax = plt.subplots(math.ceil(len(all_models)/2),2)
fig.suptitle('Distribution of Sheaf Sizes', weight = 'bold')

stats_dict = {}


for counter,modelname in enumerate(all_models):
    print(modelname)
    #model_path = path + modelname + '/generic_tt_input/'
    model_path = path + 'Denise_instances/' + modelname + '/'
    if modelname in new_models:
        sep = ';'
    else:
        sep = ','

    # read input
    ean, ean_noH, curly_H, sheaf_dict, alternatives_dict = ri.read_input(model_path, modelname, T, epsilon, zugfolge,sep)


    # analyse henkel nodes
    henkel = [v for v in ean_noH.nodes() if 'henkel' in v]
    for henkel_node in henkel:
        #print(henkel_node)
        in_nodes = list(set([rd.get_gleisbezeichnung(i) for (i,j) in ean_noH.in_edges(henkel_node)]))
        in_nodes_lines = list(set([rd.get_line(i) for (i, j) in ean_noH.in_edges(henkel_node)]))
        #print(in_nodes)
        #print(in_nodes_lines)


    nodes = ean.nodes()
    edges_noH = ean_noH.edges
    headways = [(i,j) for (i,j) in ean.edges() if ean[i][j]['type'] == 'headway']
    number_sheafs = len(list(sheaf_dict.keys()))
    inevitables = len(alternatives_dict[0]['path'])
    largest_sheaf = max([len(sheaf_dict[sheaf]) for sheaf in sheaf_dict])
    smallest_sheaf = min([len(sheaf_dict[sheaf]) for sheaf in sheaf_dict if sheaf != 0])

    info_dict = {'nodes': len(nodes),
                 'edges without headways': len(edges_noH),
                 'headways': len(headways),
                 'inevitable edges': inevitables,
                 'smallest sheaf': smallest_sheaf,
                 'largest sheaf': largest_sheaf}
    stats_dict[modelname] = info_dict



    # sizes of alternatives as bar chart
    #f,ax = plt.plot()

    i = counter // 2
    j = counter % 2

    ax[i,j].bar([i for i in range(len(sheaf_dict.keys()))],
                             [len(sheaf_dict[sheaf]) for sheaf in sheaf_dict],
                             color='b', alpha=0.5, label='# alternatives in sheaf')
    ax[i, j].set_ylabel(r"$|S|$",rotation=0, labelpad= 12,fontsize = 14)
    ax[i, j].set_xlabel("sheaf number", fontsize = 14)
    plt.sca(ax[i, j])
    plt.xticks(fontsize = 14)
    #plt.xticks(end_of_sheaf_time, end_of_sheaf_time, color='red', fontsize=8, rotation=90)
    ax[i, j].xaxis.set_major_locator(MaxNLocator(integer=True))
    plt.title(modelname, fontsize = 14)

mng = plt.get_current_fig_manager()
mng.full_screen_toggle()
path = r'/Users/deniserings/Documents/zib/s-bahn-data/scripts/DeniseMA/processed/final/images/'
plt.tight_layout()  # to fit everything in the prescribed area
# plt.show()
fig.savefig(path + 'alternatives_in_sheaf_bar_chart.png', dpi=1200)


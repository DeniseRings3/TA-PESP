#import build_ean.read_ean_functions as rd

#import scripts.DeniseMA.scripts.build_ean.read_ean_functions as rd
import build_ean.read_ean_functions as rd
def read_input(model_path, modelname, T, epsilon, zugfolge,sep = ','):

    # read EAN
    ean_file = model_path + modelname + '_ean.csv'

    ean = rd.build_EAN_from_file(ean_file, sep=sep)
    ean = rd.change_names_ean(ean)

    # ean without headways
    ean_noH = ean.copy()

    # read shared infrastructure tuples
    shared_infrastructure_file = model_path + modelname + '_shared_infrastructure_tuples.csv'
    curly_H = rd.read_shared_infrastructure_file(shared_infrastructure_file)
    curly_H = rd.change_names_curlyH(curly_H)

    # add headway arcs q3 formulation
    ean = rd.add_headway_arcs(ean, curly_H, T, epsilon, zugfolge)

    # read alternatives and sheaves
    alternatives_file = model_path + modelname + '_alternatives.csv'
    if modelname in ['BBUP_O','BBUP_W','BPKW_BKRW_BSNF_O']:
        alternatives_dict, sheaf_dict, sheaf_to_tuple = rd.read_alternatives(alternatives_file, sep = sep)
    else:
        alternatives_dict, sheaf_dict, sheaf_to_tuple = rd.read_alternatives(alternatives_file)
    alternatives_dict = rd.change_names_alternatives(alternatives_dict)

    return ean, ean_noH, curly_H, sheaf_dict,alternatives_dict
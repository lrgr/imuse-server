import pandas as pd
import numpy as np

from web_constants import *
from signatures import Signatures, get_signatures_by_mut_type
from project_data import ProjectData, get_selected_project_data

from compute_exposures import compute_exposures
from scale_samples import scale_samples

def plot_exposures(chosen_sigs, projects, mut_type, single_sample_id=None, normalize=False, tricounts_method=None):
    result = []

    exps_df = compute_exposures(chosen_sigs, projects, mut_type, single_sample_id=single_sample_id, normalize=normalize, tricounts_method=tricounts_method)
    
    default_sample_obj = dict(zip(list(exps_df.columns.values), [0] * len(list(exps_df.columns.values))))
    
    if single_sample_id == None:
        samples = scale_samples(projects)
    else:
        samples = [single_sample_id]

    exps_dict = exps_df.to_dict(orient='index')

    def create_sample_obj(sample_id):
        try:
            sample_obj = exps_dict[sample_id]
        except KeyError:
            sample_obj = default_sample_obj

        if single_sample_id == None:
            sample_obj["sample_id"] = sample_id
        return sample_obj
    
    result = list(map(create_sample_obj, samples))

    if single_sample_id != None:
        result_obj = result[0]
        result = []
        for sig, value in result_obj.items():
            result.append({
                "sig_" + mut_type: sig,
                "exp_" + mut_type + "_" + single_sample_id: value
            })

    return result
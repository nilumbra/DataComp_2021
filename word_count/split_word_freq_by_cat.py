import pandas as pd
import numpy as np
import os
import pickle

import category_dict

def split_general_wf_into_wf_by_category(gendf, categories, skip=[], persentage=0.0):
    '''
        Return a dictionary of dataframes, with key being category_id and value being the corresponding word frequency dataframe.

        Unimplemented:=[omitting words whose pos are specified by <skip> variable and whose occurrence is lower than <percentage>]
    '''
    dataframes = dict()
    mulinx = gendf.set_index(["category_id", "node_posid"]).iloc[:, 1:] # MultiIndex(["category_id", "node_posid"]), Columns: ["base", "count"]

    for category_id in categories.keys():
        dataframes[category_id] = mulinx.loc[category_id]

    return dataframes # notice since we haven't wt


def wf_by_category_id_to_csv(df, file_path):
    '''
    Do:
        write the dataframe to the specified file location as .csv 
    '''
    df.to_csv(file_path, sep=",")

def wf_by_category_id_to_pkl(df, file_path):
    '''
    Do:
        serialize the dataframe as .pkl and save to the specified file location
    '''
    with open(file_path, "wb") as file:
        pickle.dump(df, file)


if __name__ == '__main__':
    categories = category_dict.category_dict

    gen_wf = pd.read_csv("./test_count_word_in_questions.csv", sep=",")
    wf_dataframes = split_general_wf_into_wf_by_category(gen_wf, categories)


    category_group = [(1, 9, 16), (3, 11, 18), (4, 12), (5, 13), (6, 14, 99), (7, 15)]
    names = ['shibuda', 'miki', 'hori', 'mori', 'chen', 'oozuka']

    # Resulting in 6 folders, totaling 15*2 = 30 files
    for (category_ids, name) in zip(category_group, names):
        dirpath = os.path.join(os.getcwd(), name)
        os.mkdir(dirpath)
        for category_id in category_ids:
            save_to = os.path.join(dirpath, str(category_id))
            wf_by_category_id_to_csv(wf_dataframes[category_id], save_to + '.csv')
            wf_by_category_id_to_pkl(wf_dataframes[category_id], save_to + '.pkl')
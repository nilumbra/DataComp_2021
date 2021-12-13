import MeCab
import psycopg2 
from psycopg2.sql import SQL
import pandas as pd
import numpy as np 

import emoji

from collections import defaultdict
from dataclasses import make_dataclass
from pprint import pprint
from datetime import datetime, timedelta
import pickle

from concurrent.futures import ThreadPoolExecutor

def count_word_frequency_in_question(text, category_id, freq_dict, skip=range(13, 26)):
    ''' Assume inputs:
            text:= one question post to process
            category_id:= question.category_id
            freq_dict:= defaultdict(int) to store word frequency
            skip:= posid to skip, run posid.py for reference, default to auxiliary verbs

        Return:
            No return value. Will do in-place updates on freq_dict. 
            freq_dict is expected to be tuple-indexed
            (e.g. (node.surface, node.posid, category_id)=> <frequency>)
    '''

    ######## Mecab does not work perfectly with emoji. Hence do emoji-filtering with reg first##########
    emolist = []
    emofree_text = emoji.get_emoji_regexp().sub(repl=lambda m: emolist.append(m.group(0)), string=text)   
    for emoj in emolist:
        freq_dict[(emoj, 4, category_id)] += 1
    
    ######## Parse the rest#######
    node = tagger2.parseToNode(emofree_text)
    while node:
        if node.posid in skip:
            node = node.next
        else:
            if(node.posid not in range(31, 36)):
                freq_dict[(node.surface, node.posid, category_id)] += 1
            else:
                base = node.feature.split(",")[6]
                freq_dict[(base, node.posid, category_id)] += 1
            node = node.next

def word_frequency_of_questions_in_one_day(documents, date):
    '''
        Assume inputs:
            documents:= list of question posts in one day
        Return:
            pandas.DataFrame with 4 columns: ['base', 'node_posid', 'category_id', 'count']
    '''

    freq_dict = defaultdict(int) # DS to hold word freq counts in a single day
    
    # Define pos of words to skip from frequency counting 
    skip = list(range(13, 26)) 
    skip.extend([0, 5, 6, 7, 8, 9])# skip function words, symbols (except 4), and 0 

    for (category_id, content) in documents:
        count_word_frequency_in_question(content, category_id, freq_dict, skip)

    
    WordFreq = make_dataclass("WordFreq", [("base", str), ("node_posid", int), ("category_id", int), ("count", int), ("date", object)])
    freq_data = []

    freq_data = [WordFreq(key[0], key[1], key[2], item, date) for key, item in freq_dict.items()]
    freq_table = pd.DataFrame(freq_data)

    freq_table = freq_table.sort_values(by=["count"], ascending=False)
    freq_table = freq_table.set_index(["date", "category_id", "node_posid"]) # multi-indexing
    freq_table = freq_table.sort_index()

    return freq_table


if __name__ == '__main__':
    # For this to work, you need to configure mecab with mecab-ipadic-neologd dictionary first
    dicdir = '-d /usr/lib/mecab/dic/mecab-ipadic-neologd'
    tagger2 = MeCab.Tagger(dicdir)

    # Need to fill in the database password
    conn = psycopg2.connect("dbname=data_comp user=datacomp password=datacomp")
    cursor = conn.cursor()
    table = "questions" 

    start_date = datetime(2019, 1, 1)
    end_date = datetime(2021, 7, 31)
    date_range = pd.date_range(start=start_date , end=end_date, freq='D')

    word_freq_dataframe = None

    for date in date_range: # fetch all question posts in one day
        query = SQL("SELECT category_id, content FROM {} WHERE created::date= (%s);".format(table))
        cursor.execute(query, (str(date), ))
        documents = list(cursor.fetchall())

        wf_in_one_day = word_frequency_of_questions_in_one_day(documents, date)
        print(wf_in_one_day.head(20))
        # Concatenating today's word frequency to previous ones
        word_freq_dataframe = pd.concat([word_freq_dataframe, wf_in_one_day])
        print(word_freq_dataframe.tail(20))
        print(word_freq_dataframe.info())

    with open('./production_count_word_in_questions.pkl' , 'wb') as f:
        pickle.dump(word_freq_dataframe, f)
    # to pickle
    with open('./production_count_word_in_questions.csv' , 'w') as f:
        word_freq_dataframe.to_csv(path_or_buf=f, sep=',')




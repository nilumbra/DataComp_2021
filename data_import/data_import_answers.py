import picklecccccc
import pandas as d
import sqlalchemy 
import psycopg2
import conf

"""Script for import answers_xxxx.pkl into Postgresql database
   Pre-processing: replacing null characters,
                   type-casting .0 values to integers,
                   filling NaN,
                   mapping 1/0 in is_best field to True/False
"""

# Make a psycopg2 connection
# conn = psycopg2.connect("dbname=nilumbra user=nilumbra")
# conn = autocommit = True
# cur = conn.cursor()

# Creating sqlalchemy engine for postgresql
engine = sqlalchemy.create_engine(conf.uri)

# file list 
filelist = ["answers_2019.pkl", "answers_2020.pkl", "answers_2021.pkl"]

for fn in filelist:
    # Create a file stream and pickling file
    file = open(conf.filedir+fn, 'rb')
    data = pickle.load(file)

    ## Locate null characters
    # null_report = data.content.str.contains("\x00")
    # # <class 'pandas.core.series.Series'>
    # null_report = pd.DataFrame(null_report)
    # null_char_pos = null_report[null_report["content"] == True]

    # to_drop = null_char_pos.to_numpy().tolist()
    # data.drop(to_drop, axis = 0, inplace = True)
    # s.decode("utf-8", errors="replace").replace("\x00", "\uFFFD")
    #

    # Replacing null characters
    ddata = data["content"].str.replace("\x00", "") # This returns a Series of data["content"] with null characters all replaced
    data["content"] = ddata

    ## Stripping
    data.content.str.strip()

    # Filling NaN values and cast to int
    data.parent_answer_id.fillna(0, inplace=True)
    data["parent_answer_id"] = data.parent_answer_id.astype(int)
    data["is_best"] = data.is_best.astype(bool)

    data.to_sql('answers', engine, if_exists="append", index=False, chunksize=1000)

    file.close()
    del data 

# s.decode("utf-8", errors="replace").replace("\x00", "\uFFFD")
#
# ddata = data["content"].str.replace("\x00", "") # This returns a Series of data["content"] with null characters all replaced
# data["content"] = ddata
# # Checking...
# nncreport = data.content.str.contains("\x00")
# nncreport_df = pd.DataFrame(nncreport)
# nncreport_df[nncreport_df["content"] == True] 


# # answers
# data.parent_answer_id.fillna(0, inplace=True)
# data["parent_answer_id"] = data.parent_answer_id.astype(int)
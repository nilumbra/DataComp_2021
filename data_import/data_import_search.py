import pandas as pd
import sqlalchemy 
import psycopg2

import conf

# Creating sqlalchemy engine for postgresql
engine = sqlalchemy.create_engine(conf.uri)

filelist = ["search_2019.tsv", "search_2020.tsv", "search_2021.tsv"]

for fn in filelist: 
    data = pd.read_csv("../data/"+fn, sep='\t')


data.to_sql('users', engine, if_exists="append", index=False, chunksize=1000)



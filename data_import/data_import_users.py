import pandas as pd
import sqlalchemy 
import psycopg2

import conf

#"postgresql://datacomp:kant_1781@localhost:5432/datacomp"

# Creating sqlalchemy engine for postgresql
engine = sqlalchemy.create_engine(conf.uri)

fn = "./users.tsv"
data = pd.read_csv(conf.filedir+"users.tsv", sep='\t')

data.generation_id.fillna(0, inplace=True) # Replacing null values
data.generation_id = data.generation_id.astype(int) # Cast float to int

# Replacing null values
data.prefecture_id.fillna(0,inplace=True) # Replacing null values
data.prefecture_id = data.generation_id.astype(int) # Cast float to int

data.to_sql('users', engine, if_exists="append", index=False, chunksize=1000)
del data


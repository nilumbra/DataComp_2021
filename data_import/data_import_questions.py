import pickle
import pandas as pd
import sqlalchemy 
import psycopg2

import conf

# Make a psycopg2 connection
# conn = psycopg2.connect("dbname=nilumbra user=nilumbra")
# conn = autocommit = True
# cur = conn.cursor()

# Creating sqlalchemy engine for postgresql
engine = sqlalchemy.create_engine(conf.uri)

filelist = [ "questions.pkl"]
table = "questions"

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
    # data.parent_answer_id.fillna(0, inplace=True)
    # data["parent_answer_id"] = data.parent_answer_id.astype(int)
    # data["is_best"] = data.is_best.astype(bool)

    data.to_sql(table, engine, if_exists="append", index=False, chunksize=1000)

    file.close()

# cur.execute("""
#     SELECT * FROM users LIMIT 1;""")
# print(cur.fetchone())

# lc = 0 
# unpickled = None
# with open("./data/questions.pkl", 'rb') as f:
#     unpickled = pickle.load(f)
#     print(len(unpickled))


# cur.execute("""
#     INSERT INTO questions (id, user_id, category_id, content, created)
#     VALUES (%s, %s, %s, %s, %s);""",
#     (qid, uid,cid, content, created))
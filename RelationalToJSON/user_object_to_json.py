import json
from bson import json_util
import psycopg2 
import child
import answer 
import question 
import search
import user
from proxy import Proxy

conn = psycopg2.connect("dbname=datacomp user=datacomp password=kant_1781")
cursor = conn.cursor()
# cursor.execute("SELECT * FROM users LIMIT 10;")

user_id = 1377081
# users = [row for row in cursor]

# Query users (where id = u_id) and fetch one
user = user.User()
user.fillInfo(cursor, user_id) 

# # Get records by user id  
# chilren = Child.getRecordsByUserId(cursor, user_id)
# questions = Question.getRecordsByUserId(cursor, user_id)
# answers = Answer.getRecordByUserId(cursor, user_id)
# search = Search.getRecordByUserId(cursor, user_id)


# search records in [dict(s1), dict(s2)...]
tables = ["search", "children", "questions", "answers"]
for table in tables:
    if table == "search":
        user.addSearches([search.Search(s[0], s[1])._asdict() for s in Proxy.getRecordsByUserId(cursor, table, user_id)])
    elif table == "children":
        user.addChildren([child.Child(c[0], c[1], c[2])._asdict() for c in Proxy.getRecordsByUserId(cursor, table, user_id)])
    elif table == "questions":
        user.addQuestions([question.Question(q[0], q[1], q[2], q[3])._asdict() for q in Proxy.getRecordsByUserId(cursor, table, user_id)])
    elif table == "answers":
        records = Proxy.getRecordsByUserId(cursor, table, user_id)
        if records is None: 
            print("Answers is none!!!!")
        user.addAnswers([answer.Answer(a[0], a[1], a[2], a[3], a[4], a[5])._asdict() for a in records])
# answers = [answer.Answer(a[0], a[1], a[2])._asdict() for a in answer_records]
# questions = [question.Question(q[0], q[1], q[2])._asdict() for q in question_records]

# dict to json
# searches_in_json = json.dumps(search, ensure_ascii=False, default=json_util.default) # indent=2 to prettify

    
#udata_in_json = 
with open('./user_1377081', 'w') as f:
    json.dump(obj=user.__dict__, fp=f, ensure_ascii=False, indent=2, sort_keys=False, default=Proxy.json_serial_date) 
#parsed = json.loads(udata_in_json)
#print(udata_in_json)
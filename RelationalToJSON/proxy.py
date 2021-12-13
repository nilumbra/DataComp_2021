from bson import json_util
from datetime import date, datetime
import json
from psycopg2.sql import SQL

class Proxy:
    @classmethod
    def json_serial_date(cls, obj):
        """Serializing un-serializable datetime object
           Assume <obj> is a python datetime object
           Returns a JSON-serialization object
        """
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        raise TypeError ("Type %s is not serializable" % type(date))

    @classmethod
    def getRecordsByUserId(cls, cursor, table, user_id):
        # # Query children (where=user_id) fetch all 
        # for entry in children:
        #     user.addChild(Child(entry))

        # # Query questions (where=user_id)fetch all 
        # for entry in questions:
        #     user.addQuestion(Question(entry))

        # for entry in answers:
        # # Query answers (where=user_id) fecch all 
        #     user.addAnswer(Answer(entry))

        # # Query search (where=user_id) fecch all 
        # for entry in search:
        #     user.addSearch(Search(entry))
        if (table == "search"):
            query = SQL("SELECT word, created FROM {} WHERE user_id = (%s);".format(table))
            try:
                cursor.execute(query, (str(user_id), ))
            except:
                print("Error occurs as querying search")
                return None
        elif (table == "children"):
            query = SQL("SELECT id, birthday, sex FROM {} WHERE user_id = (%s);".format(table))
            try:
                cursor.execute(query, (str(user_id), ))
            except:
                print("Error occurs as querying children")
                return None
        elif (table == "questions"):
            query = SQL("SELECT id, category_id, content, created FROM {} WHERE user_id = (%s) ORDER BY id;".format(table))
            try:
                cursor.execute(query, (str(user_id), ))
            except:
                print("Error occurs as querying questions")
                return None
        elif (table == "answers"):   
            query = SQL("SELECT id, question_id, parent_answer_id, content, is_best, created FROM {} WHERE user_id = (%s) ORDER BY id;".format(table))
            print("answers called")
            try:
                cursor.execute(query, (str(user_id), ))            
            except:
                print("Error occurs as querying answers")
                return None

            
        return cursor.fetchall()


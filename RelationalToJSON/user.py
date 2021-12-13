import json
from collections import namedtuple
from psycopg2.sql import SQL
'''
{
  _id: <integer>,
  generation_id: <integer>/null,
  prefecture_id: <integer>/null,
  created: Datetime
  children: [
    {child_id: <integer>,
     birthday: Date,
     sex: 0/1/2
     }, 
     <{
     child_id: ...,
     birthday: ...,
     sex: ...
     }, ...>
  ],
  questions: [
    {qid: <integer>,  /* question_id*/
     cid: <integer>},  /* category_id*/
     content: <string>, 
     created: Datetime},
     <{...}, 
     ...>
  ],
  answers: [
    {aid: <integer>, 
     qid: <integer>,
     pid: <integer>,
     content: <string>, 
     is_best: 0/1, 
     created: Datetime
    },
    {...
    },
    ...
  ],
  
  search:[
    {word: <string>, 
     created: <Datetime>
     },
     <{...},
     ...>
  ]
}
'''
#user =  namedtuple('User', ['_id', 'generation_id', 'prefecture_id'])
class User():
    def __init__(self):
        # user_info._id
        self._id = None
        self.generation_id = None
        self.prefecture_id = None
        self.created = None

        self.children = None
        self.questions = None
        self.answers = None
        self.searches = None

    def fillInfo(self, cursor, user_id):
        query = SQL("SELECT generation_id, prefecture_id, created FROM users WHERE id = (%s);")
        cursor.execute(query, (str(user_id), ))
        user_info = cursor.fetchone() 
        self._id = user_id
        self.generation_id = user_info[0]
        self.prefecture_id = user_info[1]
        self.created = user_info[2]

    def addChildren(self, children):
        self.children = children
        
    def addQuestions(self, questions):
        self.questions = questions
        

    def addAnswers(self, answers):
        self.answers = answers
    
    def addSearches(self, searches):
        self.searches = searches
    
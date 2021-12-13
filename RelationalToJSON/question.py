from collections import namedtuple 
Question = namedtuple('Question', ['id', 'category_id', 'content', 'created'])

# class Question:
#     def __init__(self, question):
#         '''Assume <question> represents a row from questions table
#         '''
#         _id = question[0]
#         category_id = question[1]
#         content = question[2] 
#         created = question[3]


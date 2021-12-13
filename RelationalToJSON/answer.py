from collections import namedtuple 
Answer = namedtuple('Answers', ['id', 'question_id', 'parent_answer_id', 'content', 'is_best', 'created'])

# class Answer:
#     def __init__(self, answer):
#         '''Assume <question> represents a row from questions table
#         '''
#         _id = answer[0]
#         question_id = answer[1]
#         parent_answer_id = answer[2]
#         content = answer[3]
#         is_best = answer[4]
#         created = answer[5]
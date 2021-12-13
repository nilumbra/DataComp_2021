from collections import namedtuple 
Child = namedtuple('child', ['id', 'birthday', 'sex'])

# class Child:
#     def __init__(self, child):
#         _id = None
#         birthday = None
#         sex = None

#     @classmethod
#     def getRecordsByUserId(cursor, user_id):
#         cursor.execute('SELECT * FROM children WHERE user_id = %d', (user_id,))
#         return cursor.fetchAll()


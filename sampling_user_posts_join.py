import random 
import psycopg2
import pandas as pd 
import pickle
import gc

conn = psycopg2.connenct()
cur = conn.cursor()



prefectures = [1,2,3,..]
users <- SELECT * FROM users;
users_by_pref = [] 
population_by_pref = 
for i in prefectures:
    users_by_pref[i] = users[prefecture_id == i] 
    population_by_pref


# Randomly sample from users by prefectures  
prefectures_pop = {1: 1000,2:3000,3:200,}
user_post_by_prefecture = pd.dataframe("3 dimensions. Prefecture, Rows of Posts, Columns")
for pid in prefectures_pop.keys(): 
    user_id = users_by_pref[pid].first()
        for i in prefectures_pop[prefecture]
            user_post_by_prefecture[pid] <- "select * from users inner join questions on users.id = questions.user_id"    
            users_id += random.randi(5)

# Output 
#pickle.dump(user_post_by_prefecture)        
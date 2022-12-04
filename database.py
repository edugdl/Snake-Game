import pymongo
import re

def get_database():
   CONNECTION_STRING = "mongodb+srv://edu:edu123@cluster0.ugqwgad.mongodb.net/test"
   client = pymongo.MongoClient(CONNECTION_STRING)
   db = client['snakeGame']
   return db

def create_new_user(name, password):
    name = name.replace(" ","")
    password = password.replace(" ","")
    if len(password) < 6 : return False
    if not re.fullmatch(r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{6,}$", password): return False

    user = get_database()['user']
    user.insert_one({'name':name, 'password':password})
    return True

def login(user, password):
    userDb = get_database()['user']
    userList = userDb.find()
    for user_ in userList:
        if user_['name'] == user and user_['password'] == password:
            return True
    return False
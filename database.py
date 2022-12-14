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

def saveGameScore(user,score,game_type,difficulty):
    scoresDb = get_database()['scores']
    scoresDb.insert_one({'game_type':game_type,'score':score,'user':user,'difficulty':difficulty})
    return True

def getRanking(difficulty,game_type):
    scoresDb = get_database()['scores']
    scoresList = scoresDb.find()
    ranking = []
    for score in scoresList:
        if score['game_type'] == game_type and score['difficulty'] == difficulty:
            ranking.append({'user':score['user'],'score':score['score']})
    return sorted(ranking, key=lambda score: score['score'], reverse=True)
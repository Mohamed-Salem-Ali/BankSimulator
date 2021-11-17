import sqlite3 as sql
import json 
import time
from faker import Faker
import random
from random import randint
from threading import Timer
fake = Faker('ar_eg')


def commit_close_DB():
    db.commit()
    db.close()

def read_json(filename):  
    with open(filename,'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Sets file's current position at offset.
        #file.seek(0)
        return file_data



def addToUsers(users_data):
    add=0
    update=0
    for i in range(len(users_data)):
        cr.execute(f"SELECT ID FROM USERS WHERE ID = {users_data[i]['id']}")
        result = cr.fetchone()
        if result == None:
            cr.execute(f"INSERT INTO USERS (ID,NAME,AGE,ADDRESS) VALUES ( {users_data[i]['id']} ,'{users_data[i]['name']}', {users_data[i]['age']} ,'{users_data[i]['address']}') ")
            add+=1
        
        else:
            cr.execute(f"UPDATE USERS SET NAME = '{users_data[i]['name']}' , AGE = {users_data[i]['age']} , ADDRESS = '{users_data[i]['address']}' ,DATE = CURRENT_TIMESTAMP  WHERE ID = {users_data[i]['id']}  ")
            update+=1
    
    print(f"\n Added {add} Users to dataBase")
    print(f"\n Updated {update} Users to dataBase")

def addTocard(card_data):
    add=0
    update=0
    for i in range(len(card_data)):
        cr.execute(f"SELECT ID FROM CARDS WHERE ID = {card_data[i]['id']}")
        result = cr.fetchone()
        if result == None:
            cr.execute(f"INSERT INTO CARDS (ID,NAME,AGE,ADDRESS) VALUES ( {card_data[i]['id']} ,'{card_data[i]['name']}', {card_data[i]['age']} ,'{card_data[i]['address']}') ")
            add+=1
        else:
            cr.execute(f"UPDATE CARDS SET NAME = '{card_data[i]['name']}' , AGE = {card_data[i]['age']} , ADDRESS = '{card_data[i]['address']}' ,DATE = CURRENT_TIMESTAMP  WHERE ID = {card_data[i]['id']}  ")
            update+=1
    
    print(f"\n Added {add} Transactions to dataBase")
    print(f"\n Updated {update} Transactions to dataBase")


db = sql.connect("data/DataBase/Bank.db")
db.execute("CREATE TABLE IF NOT EXISTS USERS (ID NUMBER NOT NULL UNIQUE, NAME TEXT NOT NULL, AGE NUMBER NOT NULL, ADDRESS TEXT NOT NULL,DATE TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY(ID))")
db.execute("CREATE TABLE IF NOT EXISTS CARDS (TRANSACTION_ID NUMBER NOT NULL UNIQUE,  AMOUNT NUMBER NOT NULL, DATE TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY(TRANSACTION_ID))")
cr=db.cursor()
commit_close_DB()
users_data = read_json("data/UserData/users.json")
card_data= read_json("data/CardData/card.json")
db = sql.connect("data/DataBase/Bank.db")
cr=db.cursor()
#addToUsers(users_data)
try:
    while True:
        time.sleep(5)
        db = sql.connect("data/DataBase/Bank.db")
        cr=db.cursor()
        users_data = read_json("data/UserData/users.json")
        addToUsers(users_data)
        commit_close_DB()
except KeyboardInterrupt:
        
        pass
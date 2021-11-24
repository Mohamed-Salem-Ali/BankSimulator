import sqlite3 as sql
import json 
import time
from faker import Faker
import random
from random import randint
from threading import Timer
fake = Faker('ar_eg')


def commit_close_DB(db):
    db.commit()
    db.close()

def read_json(filename):  
    with open(filename,'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Sets file's current position at offset.
        file.seek(0)
        return file_data
        
def addToUsers(users_data,db,cr):
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
    print(f"\n Updated {update} Users to dataBase\n")
    print('-'*40)

def addToCard(card_data,db,cr):
    add=0
    update=0
    for i in range(len(card_data)):
        cr.execute(f"SELECT transactionId FROM CARDS WHERE transactionID = {card_data[i]['transactionId']}")
        result = cr.fetchone()
        if result == None:
            cr.execute(f"INSERT INTO CARDS (transactionId,amount,userId) VALUES ( {card_data[i]['transactionId']} , {card_data[i]['amount']} , {card_data[i]['userId']} ) ")
            add+=1
        else:
            cr.execute(f"UPDATE CARDS SET transactionId = {card_data[i]['transactionId']} , amount = {card_data[i]['amount']} , userId = {card_data[i]['userId']} ,DATE = CURRENT_TIMESTAMP  WHERE transactionID = {card_data[i]['transactionId']}  ")
            update+=1
    
    print(f"\n Added {add} Transactions to dataBase")
    print(f"\n Updated {update} Transactions to dataBase")
    print('-'*40)

def createNewDataBase():
    db = sql.connect("data/DataBase/Bank.db")
    db.execute("CREATE TABLE IF NOT EXISTS USERS (ID NUMBER NOT NULL UNIQUE, NAME TEXT NOT NULL, AGE NUMBER NOT NULL, ADDRESS TEXT NOT NULL,DATE TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY(ID))")
    db.execute("CREATE TABLE IF NOT EXISTS CARDS (TRANSACTION_ID NUMBER NOT NULL UNIQUE,  AMOUNT NUMBER NOT NULL, DATE TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY(TRANSACTION_ID))")
    cr=db.cursor()
    commit_close_DB()
 

#addToUsers(users_data)

def updateUsersDataCont():
    try:
        while True:
            time.sleep(5)
            db = sql.connect("data/DataBase/Bank.db")
            users_data = read_json("data/UserData/users.json")
            cr=db.cursor()
            addToUsers(users_data,db,cr)
            commit_close_DB(db)
    except KeyboardInterrupt: 
        pass

def updateUsersDataOnce():
    try:
        db = sql.connect("data/DataBase/Bank.db")
        cr=db.cursor()
        users_data = read_json("data/UserData/users.json")
        addToUsers(users_data,db,cr)
        commit_close_DB(db)
    except KeyboardInterrupt: 
        pass

def updateCardDataOnce():
    try:
        db = sql.connect("data/DataBase/Bank.db")
        cr=db.cursor()
        cards_data = read_json("data/CardData/card.json")
        addToCard(cards_data,db,cr)
        commit_close_DB(db)
    except: 
        pass

def updateCardDataCont():
    try:
        while True:
            time.sleep(5)
            db = sql.connect("data/DataBase/Bank.db")
            cr=db.cursor()
            cards_data = read_json("data/CardData/card.json")
            addToCard(cards_data,db,cr)
            commit_close_DB(db)
    except KeyboardInterrupt: 
        pass

def updateDataBaseCont():
    try:
        while True:
            time.sleep(5)
            db = sql.connect("data/DataBase/Bank.db")
            cr=db.cursor()
            users_data = read_json("data/UserData/users.json")
            addToUsers(users_data,db,cr)
            cards_data = read_json("data/CardData/card.json")
            addToCard(cards_data,db,cr)    
            commit_close_DB(db)
    except KeyboardInterrupt: 
        pass

def updateDataBaseOnce():
    try:
        db = sql.connect("data/DataBase/Bank.db")
        cr=db.cursor()
        users_data = read_json("data/UserData/users.json")
        addToUsers(users_data,db,cr)
        cards_data = read_json("data/CardData/card.json")
        addToCard(cards_data,db,cr)    
        commit_close_DB(db)
    except: 
        pass
    
def small_main(x):
    try:
        funcNumber = int(input(x).strip())
        if funcNumber in [1,2,3,4,5,6]: 
            if funcNumber == 1:
                updateUsersDataCont()
                
            elif funcNumber == 2:
                updateUsersDataOnce()
                   
            elif funcNumber == 3:
                updateCardDataCont()
                    
            elif funcNumber == 4:
                updateCardDataOnce()
            elif funcNumber == 5:
                updateDataBaseCont()
            elif funcNumber == 6:
                updateDataBaseOnce()
        else:
             print("\nPlease press 1 or 2 or 3 or 4 x) ") 
                
    except:
        print("\nPlease press 1 or 2 :) ")
        

def main():
    print('-'*40)
    print('\n Connect to DataBase ')
    print('\n Mohamed Salem Ali \n')
    print('-'*40)
    inputMessage = f"""
{'-'*40}
Press (1) to connect to users continuously :
press (2) to connect to users once :
Press (3) to connect to transactions continuously :
press (4) to connect to transactions once :
Press (5) to connect to DataBase continuously :
press (6) to connect to DataBase once :
======> """
    
    while True:
        try:
            small_main(inputMessage)
        except ValueError:
            print("\nPlease press 1 or 2 x) ")
            print("error")
            continue
        restart = input('\nWould you like to restart? Enter yes.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()


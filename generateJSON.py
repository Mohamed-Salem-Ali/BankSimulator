import json 
import time
from faker import Faker
import random
from random import randint
from threading import Timer
import sqlite3 as sql
fake = Faker('ar_eg')

def commit_close_DB(db):
    db.commit()
    db.close()

def writeUsersJson(numberOfData, filename):
    
    with open(filename,'r+') as file:
      
        # First we load existing data into a dict.
        file_data = json.load(file)
        # print("file1= ",file_data,len(file_data))
        index=file_data[-1]['id']
        # Join new_data with file_data inside emp_details
        for i in range(1, numberOfData+1):
            file_data.append( 
            {'id':index+i
            ,'name': fake.name()
            ,'age': random.randrange(18,100)
            ,'address':fake.address()})
        
        # Sets file's current position at offset.
        file.seek(0)
        
        # convert back to json.
        json.dump(file_data, file, indent = 4)
        #Timer(5.0,write_json(numberOfData, filename)).start()
        if numberOfData <= 0:
            print('-'*40)
            print(f"\nNo users have been added ^_^")
            print(f"\nNumber of users still {file_data[-1]['id']}\n")
            print('-'*40 ,"\n")
        else:
            print('-'*40)
            print(f"\nGenerating {numberOfData} user")   
            print(f"\nAdded {numberOfData} user to the JSON file")
            print(f"\nTotal number of users is {file_data[-1]['id']}\n")
            print('-'*40 , "\n")

def writeCardJson(numberOfData, filename):
    
    db = sql.connect("data/DataBase/Bank.db")
    cr=db.cursor()
    cr.execute("SELECT ID FROM USERS")
    result = cr.fetchall()
    commit_close_DB(db)
    if result == []:
        
        print('-'*40)
        print(f"\nNo transactions have been added ^_^")
        print(f"\nNo users in database can't generate transactions\n")
        print('-'*40 ,"\n")
    else:
        with open(filename,'r+') as file:
            
            # First we load existing data into a dict.
            file_data = json.load(file)
            # print("file1= ",file_data,len(file_data))
            index=file_data[-1]['transactionId']
            # Join new_data with file_data inside emp_details
            for i in range(1, numberOfData+1):
                file_data.append( 
                {'transactionId':index+i
                ,'amount': random.randint(100,1000000)
                ,'userId': random.randrange(1,result[-1][0])
                })
            
            # Sets file's current position at offset.
            file.seek(0)
            
            # convert back to json.
            json.dump(file_data, file, indent = 4)
            #Timer(5.0,write_json(numberOfData, filename)).start()
            if numberOfData <= 0:
                print('-'*40)
                print(f"\nNo transactions have been added ^_^")
                print(f"\nNumber of transactions still {file_data[-1]['transactionId']}\n")
                print('-'*40 ,"\n")
            else:
                print('-'*40)
                print(f"\nGenerating {numberOfData} transactions")   
                print(f"\nAdded {numberOfData} transactions to the JSON file")
                print(f"\nTotal number of Transactions is {file_data[-1]['transactionId']}\n")
                print('-'*40 , "\n")

def users_once():
    while True:
        try:
            numberOfData = int(input("\nEnter the number of users you want to generate : ").strip())   
            writeUsersJson(numberOfData,'data/userData/users.json')
            break
    
        except FileNotFoundError:
            print("fileNotFound")
            break
        except ValueError:
            print("\nNo.. input is not a number.")
            continue
        
def card_once():
    while True:
        try:
            numberOfData = int(input("\nEnter the number of transactions you want to generate : ").strip())   
            writeCardJson(numberOfData,'data/cardData/card.json')
            break
    
        except FileNotFoundError:
            print("fileNotFound")
            break
        except ValueError:
            print("\nNo.. input is not a number.")
            continue
        
def users_cont():
    while True:
        try:
            numberOfData = int(input("\nEnter the number of users you want to generate : ").strip())
            numberOfSeconds =int(input("\nEnter the number of seconds : ").strip())
            break  
        except ValueError:
            print("\nNo.. input is not a number.")
            continue
    try:
        while True:
            if numberOfData > 0:
                time.sleep(numberOfSeconds)
                writeUsersJson(numberOfData,'data/userData/users.json')
            else:
                writeUsersJson(numberOfData,'data/userData/users.json')
                break
    except ValueError:
        print("\nValueError")
    except FileNotFoundError:
        print("\nfileNotFound")
    except KeyboardInterrupt:
        pass

def card_cont():
    while True:
        try:
            numberOfData = int(input("\nEnter the number of transactions you want to generate : ").strip())
            numberOfSeconds =int(input("\nEnter the number of seconds : ").strip())
            break  
        except ValueError:
            print("\nNo.. input is not a number.")
            continue
    try:
        while True:
            if numberOfData > 0:
                time.sleep(numberOfSeconds)
                writeCardJson(numberOfData,'data/cardData/card.json')
            else:
                writeCardJson(numberOfData,'data/cardData/card.json')
                break
    except ValueError:
        print("\nValueError")
    except FileNotFoundError:
        print("\nfileNotFound")
    except KeyboardInterrupt:
        pass

def json_cont():
    while True:
        try:
            numberOfDataU = int(input("\nEnter the number of users you want to generate : ").strip())   
            numberOfDataC = int(input("\nEnter the number of transactions you want to generate : ").strip())
            numberOfSeconds =int(input("\nEnter the number of seconds  : ").strip())
            break  
        except ValueError:
            print("\nNo.. input is not a number.")
            continue
    try:
        while True:
            if numberOfDataU > 0:
                time.sleep(numberOfSeconds)
                writeCardJson(numberOfDataC,'data/cardData/card.json')
                writeUsersJson(numberOfDataU,'data/userData/users.json')
            else:
                writeCardJson(numberOfDataC,'data/cardData/card.json')
                writeUsersJson(numberOfDataU,'data/userData/users.json')
                break
    except ValueError:
        print("\nValueError")
    except FileNotFoundError:
        print("\nfileNotFound")
    except KeyboardInterrupt:
        pass

def json_once():
    while True:
        try:
            numberOfDataU = int(input("\nEnter the number of users you want to generate : ").strip())   
            numberOfDataC = int(input("\nEnter the number of transactions you want to generate : ").strip())  
            writeCardJson(numberOfDataC,'data/cardData/card.json')
            writeUsersJson(numberOfDataU,'data/userData/users.json')
            break
    
        except FileNotFoundError:
            print("fileNotFound")
            break
        except ValueError:
            print("\nNo.. input is not a number.")
            continue

def small_main(x):
    try:
        funcNumber = int(input(x).strip())
        if funcNumber in [1,2,3,4,5,6]: 
            if funcNumber == 1:
                users_cont()
                     
            elif funcNumber == 2:
                users_once()
                        
            elif funcNumber == 3:
                card_cont()
                        
            elif funcNumber == 4:
                card_once()
            elif funcNumber == 5:
                json_cont()
            elif funcNumber == 6:
                json_once()
        else:
             print("\nPlease press 1,2,3,4,5,6 x) ")                
    except:
        print("\nNo.. input is not a number.")


def main():
    print('-'*40)
    print('\n Generate JSON data ')
    print('\n Mohamed Salem Ali \n')
    print('-'*40)
    inputMessage = f"""
{'-'*40}
Press (1) to add users continuously :
press (2) to add users once :
press (3) to add transactions continuously :
press (4) to add transactions once :
press (5) to add transactions and users continuously :
press (6) to add transactions and users once :
======> """
    while True:
        try:
            small_main(inputMessage)
        except ValueError:
            print("\nPlease press 1 or 2 or 3 or 4 x) ")
            continue
        restart = input('\nWould you like to restart? Enter yes.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()

#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json 
import time
from faker import Faker
import random
from random import randint
from threading import Timer


# In[2]:


fake = Faker('en_US')
user_data=[]


# In[3]:


def write_json(numberOfData, filename):
    
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

def users_once():
    while True:
        try:
            numberOfData = int(input("\nEnter the number of users you want to generate : ").strip())   
            write_json(numberOfData,'data/userData/users.json')
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
                write_json(numberOfData,'data/userData/users.json')
            else:
                write_json(numberOfData,'data/userData/users.json')
                break
    except ValueError:
        print("\nValueError")
    except FileNotFoundError:
        print("\nfileNotFound")
    except KeyboardInterrupt:
        pass
def small_main(x):
        try:
            funcNumber = int(input(x).strip())
            if funcNumber in [1,2]: 
                if funcNumber == 1:
                    users_cont()
                elif funcNumber == 2:
                    users_once()
            else:
                print("1 or 2 Onlyyyy XD")
        except:
            print("\nPlease press 1 or 2 :) ")


def main():
    print('-'*40)
    print('\n Generate JSON data for users ')
    print('\n Mohamed Salem Ali \n')
    print('-'*40)
    inputMessage = f"""
{'-'*40}
Press (1) to add users every continuously :
press (2) to add users once :
======> """
    while True:
        try:
            small_main(inputMessage)
        except ValueError:
            print("\nPlease press 1 or 2 x) ")
            continue
        restart = input('\nWould you like to restart? Enter yes.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()


# In[ ]:





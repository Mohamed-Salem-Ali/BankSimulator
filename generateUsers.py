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
            print(f"\nno users have been added ^_^")
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
            numberOfData = int(input("\nEnter the number of users you want to generate : "))   
            write_json(numberOfData,'data/userData/users1.json')
            break
        except ValueError:
            print("\nNo.. input is not a number.")
            continue
        break

def small_main(funcNumber):
    while True:
        try:
            if funcNumber in [1,2]: 
                if funcNumber == 1:
                    print("continue phase")
                    break
                elif funcNumber == 2:
                    users_once()
                    break
        except:
            print("\nPlease press 1 or 2 :) ")
            continue


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
            functionNumber = int(input(inputMessage).strip())
            small_main(functionNumber)
        except ValueError:
            print("\nPlease press 1 or 2 :) ")
            continue
        restart = input('\nWould you like to restart? Enter yes.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()


# In[ ]:





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
        print(f"\n Added {numberOfData} user to the JSON file")
        print(f"\n Total number of users is {file_data[-1]['id']}")
 


# In[1]:


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
            {'-'*40}
            if functionNumber in [1,2]:
                print("phase 1")
            else:
                print("error in phase 1")    
            numberOfData = int(input("\nEnter the number of users you want to generate : "))
            print(f"\nGenerating {numberOfData} user")
            write_json(numberOfData,'data/userData/users1.json')
        except ValueError:
            print("\nNo.. input is not a number.")
            continue
        except EOFError:
            restart = input('\nWould you like to restart? Enter yes.\n')
            if restart.lower() != 'yes':
                break


if __name__ == "__main__":
	main()


# In[ ]:





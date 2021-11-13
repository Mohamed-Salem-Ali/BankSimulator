import json 
import time
from faker import Faker
import random
from random import randint
fake = Faker('en_US')
user_data=[]

def createRandomData(dataNumber):
    for i in range(dataNumber):
        user_data.append(
        {'id':i+1
        ,'name': fake.name()
        ,'age': random.randrange(18,100)
        ,'address':fake.address()})

def write_json(new_data, filename='users.json'):
    with open(filename,'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        print("file1= ",file_data)
        # Join new_data with file_data inside emp_details
        file_data["users"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)
 
createRandomData(10)

write_json(user_data[1])
# file = "users.json"
# def write_json(data,fileName="users.json"):
#     with open(fileName,'w') as f:
#         json.dump(data,f,indent=4)
#write_json(user_data[2])
#print(user_data[2])
#for i in range(len(user_data)): 
#   print(user_data[i],"\n")
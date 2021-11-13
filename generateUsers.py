import json 
import time
from faker import Faker
import random
from random import randint
fake = Faker('en_US')
user_data=[]
for _ in range(10):
    user_data.append({'name': fake.name(),'age': randint(0, 100),'poo': float(random.randrange(155, 389))/100 })
#for i in range(len(user_data)): 
#   print(user_data[i],"\n")
file = "users.json"
def write_json(data,fileName="usersData.json"):
    with open(fileName,'w') as f:
        json.dump(data,f,indent=4)
write_json(user_data)
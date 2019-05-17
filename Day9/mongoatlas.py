"""
Code Challenge 2
Perform similar steps as in the above code challenge but store the contents in 
an online mongo atlas database.
"""


import pymongo
#import dns # required for connecting with SRV

#client = pymongo.MongoClient("mongodb://K_Vaid:123chandu30%26@cluster0-shard-00-00-tofyu.mongodb.net:27017,cluster0-shard-00-01-tofyu.mongodb.net:27017,cluster0-shard-00-02-tofyu.mongod
client = pymongo.MongoClient("mongodb://sky123:skyhigh1710@cluster0-shard-00-00-ucrt4.mongodb.net:27017,cluster0-shard-00-01-ucrt4.mongodb.net:27017,cluster0-shard-00-02-ucrt4.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")


mydb = client.Employee

def add_student(idd,name, age, branch):
    mydb.Employees.insert_one(
            {
            "id" : idd,
            "name" : name,
            "age" : age,
            "branch" : branch
            })
    return "Student added successfully"


def fetch_all_students():
    user = mydb.Employees.find()
    for i in user:
        print (i)




add_student(1,'Shyam', 20, 'CSE')
add_student(2,'Yogi', 19, 'Mech')
add_student(3,'Ram', 18, 'ECE')
add_student(4,'Karan', 21, 'EE')
add_student(5,'Dev', 22, 'Civil')

fetch_all_students()
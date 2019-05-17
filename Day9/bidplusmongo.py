"""
Code Challenge 3
In the Bid plus Code Challenege 

          1. BID NO
          2. items
          3. Quantity Required
          4. Department Name And Address
          5. Start Date/Time(Enter date and time in different columns)
          6. End Date/Time(Enter date and time in different columns)

Store the information into a database mySQL Database
"""

import pymongo
from  selenium import webdriver
from time import sleep


client = pymongo.MongoClient("mongodb://sky123:skyhigh1710@cluster0-shard-00-00-ucrt4.mongodb.net:27017,cluster0-shard-00-01-ucrt4.mongodb.net:27017,cluster0-shard-00-02-ucrt4.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")


mydb = client.Employee



url = "https://bidplus.gem.gov.in/bidlists"

browser = webdriver.Chrome("C:/forsk/chromedriver.exe")
browser.get(url)


sleep(2)

A=[]
B=[]
C=[]
D=[]

for i in range(1,11):
    A.append(browser.find_element_by_xpath("//*[@id='pagi_content']/div["+str(i)+"]/div[1]/p[1]/a").text)    
    B.append(browser.find_element_by_xpath("//*[@id='pagi_content']/div["+str(i)+"]/div[2]/p[1]/span").text)
    C.append(browser.find_element_by_xpath("//*[@id='pagi_content']/div["+str(i)+"]/div[2]/p[2]/span").text)
    D.append(browser.find_element_by_xpath("//*[@id='pagi_content']/div["+str(i)+"]/div[3]/p[1]").text)

def add_item(A,B,C,D):
    for i in range(0,10):
        mydb.Employees.insert_one(
            {
                    "BidNo" : A[i],
                    "Items" : B[i],
                    "Quantity" : C[i],
                    "Dept" : D[i]
            })
        return "Item added successfully"

def fetch_all_items():
    user = mydb.Employees.find()
    for i in user:
        print (i)
        
add_item(A,B,C,D)
fetch_all_items()
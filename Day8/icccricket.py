
"""
Code Challenge
  Name: 
    Webscrapping ICC Cricket Page
  Filename: 
    icccricket.py
  Problem Statement:
    Write a Python code to Scrap data from ICC Ranking's 
    page and get the ranking table for ODI's (Men). 
    Create a DataFrame using pandas to store the information.
  Hint: 
    https://www.icc-cricket.com/rankings/mens/team-rankings/odi 
    
    
    #https://www.icc-cricket.com/rankings/mens/team-rankings/t20i
    #https://www.icc-cricket.com/rankings/mens/team-rankings/test
"""


from bs4 import BeautifulSoup
import requests
#import urllib






#specify the url
wiki = "https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting"
source = requests.get(wiki).text
#or
#source = urllib.request.urlopen(wiki)

soup = BeautifulSoup(source,"lxml")

print (soup.prettify())

all_tables=soup.find_all('table')

print (all_tables)


right_table=soup.find('table', class_='table rankings-table')

print (right_table)

source = requests.get(wiki).text
A=[]
B=[]
C=[]
for row in right_table.find_all('tr'):
     col= row.findAll('td')
     print(len(col))
     if len(col) == 4:
        A.append(col[0].text.strip())
        B.append(col[1].text.strip())
        C.append(col[2].text.strip())
        
import pandas as pd
from collections import OrderedDict

col_name = ["Rank","Player Nmae","points"]
col_data = OrderedDict(zip(col_name,[A,B,C]))
df = pd.DataFrame(col_data) 
df.to_csv("former.csv")

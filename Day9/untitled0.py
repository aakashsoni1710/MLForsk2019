"""
Code Challenge 4

Scrap the data from the URL below and store in sqlite database

https://www.icc-cricket.com/rankings/mens/team-rankings/odi


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


right_table=soup.find('table', class_='table rankings-table')

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
        
import sqlite3
from pandas import DataFrame

#os.chdir('/Users/sylvester/Desktop/Database and Python/Python/')

# File based database ( connects if exits or creates a new one if it does not exists ) 
conn = sqlite3.connect ( 'icc.db' )


# creating cursor
c = conn.cursor()


# STEP 1
# www.sqlite.org/datatype3.html
c.execute ("""CREATE TABLE Players(
          ranking INTEGER,
          name  TEXT,
          country TEXT
          )""")


# STEP 2
for i in range(0,10):
    c.execute("INSERT INTO Players VALUES ("+A[i]+","+B[i]+","+C[i]+")")

# STEP 3
c.execute("SELECT * FROM Players")
# "SELECT * FROM employees WHERE last = 'Fernandes' "



# STEP 4
# returns one or otherwise None as a tuple
print ( c.fetchone()) 

# returns one or otherwise None as a tuple
print ( c.fetchmany(2)) 

print ( c.fetchall() )


c.execute("SELECT * FROM Players")

df = DataFrame(c.fetchall())  # putting the result into Dataframe
df.columns = ["Ranking","Name","Contry"]

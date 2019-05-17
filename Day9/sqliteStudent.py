
"""

Code Challenge 1
Write a python code to insert records to a mongo/sqlite/MySQL database 
named db_University for 10 students with fields like 
Student_Name, Student_Age, Student_Roll_no, Student_Branch.

"""

import sqlite3
from pandas import DataFrame

#os.chdir('/Users/sylvester/Desktop/Database and Python/Python/')

# File based database ( connects if exits or creates a new one if it does not exists ) 
conn = sqlite3.connect ( 'student.db' )


# creating cursor
c = conn.cursor()


# STEP 1
# www.sqlite.org/datatype3.html
c.execute ("""CREATE TABLE students(
          id INTEGER,
          name  TEXT,
          branch TEXT,
          year INTEGER
          )""")


# STEP 2
c.execute("INSERT INTO students VALUES (01,'Akash Soni', 'CSE', 2)")
c.execute("INSERT INTO students VALUES (02,'Yogendra', 'ME', 3)")
c.execute("INSERT INTO students VALUES (03,'Pradeep', 'ECE', 1)")
c.execute("INSERT INTO students VALUES (04,'Kunal', 'CSE',4)")
c.execute("INSERT INTO students VALUES (05,'Devendra', 'Civil',3)")


# STEP 3
c.execute("SELECT * FROM students")
# "SELECT * FROM employees WHERE last = 'Fernandes' "



# STEP 4
# returns one or otherwise None as a tuple
print ( c.fetchone()) 

# returns one or otherwise None as a tuple
print ( c.fetchmany(2)) 

print ( c.fetchall() )


c.execute("SELECT * FROM students")

df = DataFrame(c.fetchall())  # putting the result into Dataframe
df.columns = ["Sid","Name","Branch","year"]

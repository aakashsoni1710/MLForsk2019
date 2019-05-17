
"""
Code Challenge
  Name: 
    Create a list of absentee
  Filename: 
    absentee.py
  Problem Statement:
    Make a program that create a file absentee.txt
    The program should take max 25 students name one by one
    When the user enter a blank line, it should terminate the input
    Store all the name of students in the file    
    Once all the students names have been entered, it should display the list
    
"""

with open("absentee.txt",mode="w") as fp1:
    count=0
    for stu in range(0,25):
        if count<25:
            abs=input("Enter the absentee name:")
            fp1.write(abs+"\n")
            count=count+1
            if (abs==""):
                break
        else:
            print("Max Limit")
            break
     
with open("absentee.txt",mode="r") as fp1:
    fp1.seek(0,0)
    for stu in fp1.readlines():
        print(stu)
            
            
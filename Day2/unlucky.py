"""
Code Challenge
  Name: 
    Unlucky 13
  Filename: 
    unlucky.py
  Problem Statement:
    Return the sum of the numbers in the array, returning 0 for an empty array. 
    Except the number 13 is very unlucky, so it does not count and numbers that 
    come immediately after a 13 also do not count
    Take input from user  
  Input: 
    13, 1, 2, 13, 2, 1, 13
  Output:
    3
"""


list1=input("Enter a list of integers").split(" ")
sum=0
for i in list1:
    
    if(i=="13"):
        continue
    if(list1[=="13"):
        continue
    
    sum=int(i)+sum
    
print(sum)

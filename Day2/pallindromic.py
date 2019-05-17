"""
Code Challenge
  Name: 
    Pallindromic Integer
  Filename: 
    pallindromic.py
  Problem Statement:
    You are given a space separated list of integers. 
    If all the integers are positive and if any integer is a palindromic integer, 
    then you need to print True else print False.
    (Take Input from User)  
  Hint: 
      A palindromic number or numeral palindrome is a number that remains the same
      when its digits are reversed. 
      Like 16461, for example, it is "symmetrical"
      Shorter logic can be developed using any and all and List comprehension
  Input: 
    12 9 61 5 14
  Output:
    True
"""

list1=input("Enter the list of integers:").split(" ")
print(list1)

for l1 in list1:
    if(int(l1) < 0):
        ans="False"
        break
    elif(int(l1)<10):
        ans="True"
        break
    elif(l1==l1[::-1]):
        ans="True"
        break
    else:
        ans="False"
print(ans)

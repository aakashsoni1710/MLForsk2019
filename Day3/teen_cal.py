
"""
Code Challenge
  Name: 
    Teen Calculator
  Filename: 
    teen_cal.py
  Problem Statement:
    Take dictionary as input from user with keys, a b c, with some integer 
    values and print their sum. However, if any of the values is a teen -- 
    in the range 13 to 19 inclusive -- then that value counts as 0, except 
    15 and 16 do not count as a teens. Write a separate helper "def 
    fix_teen(n):"that takes in an int value and returns that value fixed for
    the teen rule. In this way, you avoid repeating the teen code 3 times  
  Input: 
    {"a" : 2, "b" : 15, "c" : 13}
  Output:
    Sum = 17
"""

list1=input("Enter the list od char:").split(" ")
list2= input("Enter the integer values:").split(" ")
    
dict1=dict(zip(list1,list2))

print(dict1)

list4=list(dict1.values())
a=len(list4)
l1=["13","14","17","18","19"]
sum=0
for i in range(0,a):
    if list4[i] not  in l1:
        sum=sum+int(list4[i])
    else:
        continue

print(sum)
        
        
    


    
    
"""
Code Challenge
  Name: 
    Operations Function
  Filename: 
    operation.py
  Problem Statement:
    Write following functions for list operations. Take list as input from the User
    Add(), Multiply(), Largest(), Smallest(), Sorting(), Remove_Duplicates(), Print()
    Only call Print() function to display the results in the below displayed 
    format (i.e all the functions must be called inside the print() function 
    and only the Print() is to be called in the main script)

  Input: 
    5,2,6,2,3
  Output:
    Sum = 18
    Multiply = 360
    Largest = 6
    Smallest = 2
    Sorted = [2, 2, 3, 5, 6]
    Without Duplicates = [2, 3, 5, 6]  
"""
def Pprint(l1):
    print("Sum="+add(l1))
    print("Multiply="+multiply(l1))
    print("Largest="+largest(l1))
    print("Smallest="+smallest(l1))
    print("sorting="+sorting(l1))
    #rem_dep(l1)
    
    
def add(l1):
    sum=0
    for i in l1:
        sum=int(i)+sum
    return str(sum)
def multiply(l1):
    
    mul=1
    for i in l1:
        mul=int(i)*mul
    return str(mul)
def largest(l1):
    large=l1[0]
    for i in l1:
        if int(i)>int(large):
            large=int(i)
    return str(large)
        
def smallest(l1):
    small=l1[0]
    for i in l1:
        if int(i)<int(small) :
            small=int(i)
    return str(small)
def sorting(l1):
    l1.sort()
    return str(l1)
def rem_dep(l1):
    pass







list1=input("Enter a list of integers").split(" ")
Pprint(list1)

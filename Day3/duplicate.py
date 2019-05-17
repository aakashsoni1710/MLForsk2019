"""
Code Challenge
  Name: 
    Duplicate
  Filename: 
    duplicate.py
  Problem Statement:
    With a given list [12,24,35,24,88,120,155,88,120,155]
    Write a program to print this list after removing all duplicate values 
    with original order reserved  
"""

list1=[12,24,35,24,88,120,155,88,120,155]
set1=set(list1)

l1=list(set1)
l1.reverse()
print(l1)
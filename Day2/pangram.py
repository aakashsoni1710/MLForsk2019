"""
Code Challenge
  Name: 
    Pangram
  Filename: 
    pangram.py
  Problem Statement:
    Write a Python function to check whether a string is PANGRAM or not
    Take input from User and give the output as PANGRAM or NOT PANGRAM.
  Hint:
    Pangrams are words or sentences containing every letter of the alphabet at least once.
    For example: "The quick brown fox jumps over the lazy dog"  is a PANGRAM.
  Input: 
    The five boxing wizards jumps.
  Output:
    NOT PANGRAM
"""
import string 
str1=input("Enter the string:")
print(str1)
count=0

str2=string.ascii_lowercase
a=len(str1)
if(a<26):
    print("It is not a pangram.")
else:
    for i in range(0,26):
        if str2[i] in str1:
            count=count+1
            print(count)
            continue
        else:
            break
        
    
if count==26:
    print("It is a Pamnagram")
else:
    print("Not a panagram")
"""
Code Challenge
  Name: 
    copy command
  Filename: 
    copy.py
  Problem Statement:
    Make a program that create a copy of a file    
"""

fp=open("new.txt","rt")
fp1=open("new1.txt","w")
fp.seek(0,0)
fp1.write(fp.read())
fp1.close()
fp.close()
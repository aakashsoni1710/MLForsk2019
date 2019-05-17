"""
Code Challenge
  Name: 
    Word count
  Filename: 
    wordcount.py
  Problem Statement:
    Unix systems contain many utility functions. 
    One of the most useful to me is wc, the "word count" program. 
    If you run wc against a text file, it'll count the characters, words, 
    and lines that the file contains.
     
    The challenge for this exercise is to write a version of wc in Python. 
    However, your version of wc will return four different types of information 
    about the files:
 
        Number of characters (including whitespace)
        Number of words (separated by whitespace)
        Number of lines
        Number of unique words
    
    The program should ask the user for the name of an input file, 
    and then produce output for that file. 
    
"""

no_of_char=0
no_of_lines=0
no_of_words=0
no_of_unique_words=0
file_name=input("Enter the file name:")

with open(file_name) as fp1:
    for line in fp1.readlines():
        for i in line:
            no_of_char=no_of_char+1
        no_of_words=no_of_words+len(line.split(" "))
        no_of_lines=no_of_lines+1
            
        no_of_unique_words=no_of_unique_words+len(set((line.split(" "))))
    
print(no_of_char)
print(no_of_words)
print(no_of_lines)
print(no_of_unique_words)



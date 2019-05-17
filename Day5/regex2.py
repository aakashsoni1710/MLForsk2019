"""

Code Challenge
  Name: 
    Regular Expression 2
  Filename: 
    regex2.py
  Problem Statement:
    You are given N email addresses. 
    Your task is to print a list containing only valid email addresses in alphabetical order.
    Valid email addresses must follow these rules:

    It must have the username@websitename.extension format type.
    The username can only contain letters, digits, dashes and underscores.
    The website name can only have letters and digits.
    The minimum length is 2 and maximum length of the extension is 4. 
  Hint: 
    Using Regular Expression 
  Input:
    lara@hackerrank.com
    brian-23@hackerrank.com
    britts_54@hackerrank.com
  Output:
    ['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']

"""

import re
email_list=[]
varified_email_list=[]
while True:
    
    email_id=input("Enter the email Id:")
    email_list.append(email_id)
    
    #print(email_list)
    
    if not email_id:
        break

for email in email_list:
    if re.findall(r'[a-zA-Z-_]*[0-9]*@[a-z0-9]+\.[a-z]{2,4}',email):
        varified_email_list.append(email)
print(varified_email_list)
    
    

"""

Code Challenge
  Name: 
    Regular Expression 4
  Filename: 
    regex4.py
  Problem Statement:
    You are given email addresses. 
    Your task is to print a list containing only valid email addresses in lexicographical order .
    (Take input from User)

    Valid email addresses must follow these rules:

    It must have the username@websitename.extension format type.
    The username can only contain letters, digits, dashes and underscores. 
    The website name can only have letters and digits. 
    The maximum length of the extension is  
 
  Hint: 
    Using Regular Expression 
  Input:
    ajeet@forsk.com
    kunal-23@forsk.com
    yogendra_54@forsk.com
  Output:
    ['ajeet@forsk.com', 'kunal-23@forsk.com', 'yogendra_54@forsk.com’]

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
varified_email_list.sort()
for i in varified_email_list:
    print(i)
    
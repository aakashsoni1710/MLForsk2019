"""
Code Challenge
  Name: 
    Currency Converter Convert  from USD to INR
  Filename: 
    currecncyconv.py
  Problem Statement:
    You need to fetch the current conversion prices from the JSON  
    using REST API
  Hint:
    http://free.currencyconverterapi.com/api/v5/convert?q=USD_INR&compact=y
    Check with http://api.fixer.io/latest?base=USD&symbol=EUR
    
"""

import requests

amount=float(input("Enter the amount in USD:"))
url ="https://free.currconv.com/api/v7/convert?q=USD_INR&compact=ultra&apiKey=d835a4639fdc0ac0b538"
print (url)

response=requests.get(url)
response.content

jsondata = response.json()
print(jsondata)


INR=jsondata["USD_INR"]
print(amount*INR)

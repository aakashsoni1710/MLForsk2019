"""
Code Challenge
  Name: 
    JSON Parser
  Filename: 
    json.py
  Problem Statement:
    Get me the other details about the city
        Latitude and Longitude
        Weather Condition
        Wind Speed
        Sunset Rise and Set timing
"""
#api.openweathermap.org/data/2.5/weather


import requests

url1 = "http://api.openweathermap.org/data/2.5/weather"
url2 = "?q=Jaipur"
url3 = "&appid=16ac1a7ddc5f2e2a8da5b680ce118394"

url = url1 + url2 + url3
print (url)

response = requests.get(url)
# requests.get(url,params={"q":"Jaipur", "appid"="e9185b28e9969fb7a300801eb026de9c"})
response.content

# Content in binary form
print (type(response.content))

jsondata = response.json()

print("Longitude:",jsondata["coord"]["lon"])
print("Latitude:",jsondata["coord"]["lat"])

print("Weather Conditions:")
print(jsondata["weather"][0]["description"])


print("Sunrise:",jsondata["sys"]["sunrise"])
print("Sunset:",jsondata["sys"]["sunset"])


"""
Code Challenge
  Filename: 
    height.py
  Problem Statement:

people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]

height_total = 0
height_count = 0
for person in people:
    if 'height' in person:
        height_total += person['height']
        height_count += 1

if height_count > 0:
    average_height = height_total / height_count

    print (average_height)
    
Try rewriting the code below using map, reduce and filter. 
Filter takes a function and a collection. 
It returns a collection of every item for which the function returned True.
    

"""
from functools import reduce
people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]

person=list(filter(lambda value:'height' in value,people))
#print(person)

hieght=dict(map(lambda value:value.values(),person))
#print(hieght)

dict_len=len(hieght)
#print(dict_len)
avg=reduce(lambda h,w:h+w,hieght.values())
avg1=avg/dict_len
print("Average height:",avg1)
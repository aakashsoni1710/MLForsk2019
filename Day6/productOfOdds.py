
"""
This Python function accepts a list of numbers and computes the product of all the odd numbers:

def productOfOdds(list):
    result = 1
    for i in list:
        if i % 2 == 1:
            result *= i
    return result
    
Rewrite the Python code using map, filter, and reduce:

def productOfOdds(list):
    return reduce(r_func, filter(f_func, map(m_func, list)))

    
"""


from functools import reduce

def productOdds():
    print ("Result:",reduce(lambda x,y:x*y,list(filter(lambda x:x%2==1,list(map(int,input("Enter the list of no.:").split(" ")))))))
productOdds()

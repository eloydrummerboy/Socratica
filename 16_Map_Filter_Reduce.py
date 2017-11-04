# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 16:12:42 2017

@author: eloy
"""

# Map, Filter, Reduce

import math

def area(r):
    """Area of a circle with readius 'r'."""
    return math.pi * (r**2)
    
# What if we need to compute the areas for multiple circles?
radii = [2,5,7.1,0.3,10]

# Method 1: Direct method

areas = []
for r in radii:
    a = area(r)
    areas.append(a)
    
print(areas)


# Method 2: use 'map' function

map(area,radii) # This returns a map object, which is an iterator

# To see the list, we need to pass the map into the list constructor
list(map(area,radii))

temps = [("Berlin", 29), ("Cairo", 36), ("Buenos Aires", 19),
         ("Los Angeles", 26),("Tokyo",27), ("New York", 28),
         ("London",22), ("Beijing", 32)]
         
c_to_f = lambda data: (data[0], (9/5)*data[1] + 32)

list(map(c_to_f,temps))

# Filter Function
# Use case, select all values above the average

import statistics

data = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
avg = statistics.mean(data)

filter(lambda x: x>avg, data)
# Again, this retuns a filter object, an iterable, not a list

list(filter(lambda x: x>avg, data))

# Use Case 2: Remove missing data

countries = ["","Argentina","","Brazil","Chile","","Colombia","","Ecuador","","","Venezuela"]

list(filter(None, countries))

# Here, None menas there is no supplied function. The data itself
# acts as the function. So all values will get passed through
# except those that Python interprets as False. Which are most variations 
# of empty sets, nulls, 0, {}, (), {}, etc.


# Reduce
# As of Python 3, it is no longer a builtin function, it has been
# demoted to the functools module
from functools import reduce
# Multiply all numbers in a list
data = [2,3,5,7,11,13,17,19,23,29]
# Need a function that takes in two imputs
multiplier = lambda x,y: x*y
reduce(multiplier,data)

product = 1
for x in data:
    product = product*x
print(product)





    


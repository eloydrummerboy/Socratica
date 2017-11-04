# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 21:00:53 2017

@author: eloy
"""

print("# Random Number Generator")
print("# The Random Module")

import random

print("# random.random returns random value in interval [0,1)")

print("# Display 10 random numbers from [0,1)")
for i in range(10):
    print(random.random())
    
print("# Generate random numbers from interval [3,7)")

def my_random():
    # Random, scale, shift, return...
    return 4*random.random() + 3
    
for i in range(10):
    print(my_random())

print("# Easier way, uniform function")
for i in range(10):
    print(random.uniform(3,7))


print("# Generate 20 numbers from Normal Distribution (Bell Curve)")
print("# with mean 0 and standard deviation 1")

for i in range(20):
    print(random.normalvariate(0,1))    
    
    
print("# Simulate roll of 6-sided die")
    
for i in range(20):
    print(random.randint(1,6))
    
print("# Random selection from a list of value")
print("# For instance, Rock / Paper / Scissors")   

for i in range(20):
    print(random.choice(["Rock","Paper","Scissors"]))
    
    
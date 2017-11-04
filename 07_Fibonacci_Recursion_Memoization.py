# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 20:24:57 2017

@author: eloy
"""
# memoization done the manual way
fibonacci_cache = {}

def fibonacci(n):
    # If we have cached the value, then return it
    if n in fibonacci_cache:
        return fibonacci_cache[n]
        
    # Compute the Nth Term  
    if n==1:
        value =  1
    elif n==2:
        value = 1
    elif n>2:
        value = fibonacci(n-1) + fibonacci(n-2)
        
    # Cache value then return it
    fibonacci_cache[n] = value
    return value
        
for n in range(1,1001):
    print(n, ":", fibonacci(n))
    
    
# Memoization done the easy way
from functools import lru_cache
# Least Recently Used Cache

@lru_cache(maxsize=1000)
def fibonacci2(n):
    # Check that input is a positive integer
    if type(n) != int:
        raise TypeError("n must be a positive int")
    if n < 1:
        raise ValueError("n must be a positive int")
    
    # Compute the Nth term
    if n==1:
        return 1
    elif n==2:
        return 1
    elif n>2:
        return fibonacci2(n-1) + fibonacci2(n-2)
        
for n in range(1,1001):
    print(n, ":", fibonacci2(n))


# See how ratio between consequtive fibonnaci numbers
# approaches the Golden Ratio
for n in range(1,51):
    print(fibonacci2(n+1) / fibonacci2(n))     
    
    
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Prime Numbers

# ONly divisible by itself and 1

# Write function to tell if a number is Prime

# Version 1: Test all divisors from 2 through n-1

def is_prime_v1(n):
    """Return 'True' if 'n' is a prime number. False otherwise."""
    if n == 1:
        return False
    
    for d in range(2,n):
        if n%d == 0:
            return False
    return True
    
    
# ===== Test Function =====
import sys

RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"

for n in range(1,21):
    isPrime = is_prime_v1(n)
    if isPrime:  
        sys.stdout.write(BOLD + RED)
        print( n, isPrime)
        sys.stdout.write(RESET)      
    else:
        print(n, isPrime)

    
 # how fast is this method?
import time

t0 = time.time()
for n in range(1,100000):
    is_prime_v1(n)
t1 = time.time()
print("Time required: ", t1-t0)
    
# Time required:  212.39803647994995

    
# Now let's use a trick, not that the divisors of 
# any number start to repeat at sqrt(n) x sqrt(n)
# 36 = 1*46
#    = 2*18    
#    = 3*12
#    = 4*9
#    = 6*6 <--- sqrt(n) * sqrt(n)
#    = 9*4
#    = 12*3  
#    = 18*2
#    = 36*1  
# so we only have to check up to sqrt(n), not n-1 becaues
# if, for instance, 36 is not divisible by anything up to that
# point, it must be prime, because if it were divisible by anything
# larger than sqrt(n), the other divisor would have to be smaller than 
# sqrt(n), and we would have found it already.

import math

def is_prime_v2(n):
    """Return 'True' if 'n' is a prime number. False otherwise."""
    if n == 1:
        return False
    
    for d in range(2,int(math.sqrt(n))):
        if n%d == 0:
            return False
    return True
 
# how fast is this method?
import time

t0 = time.time()
for n in range(1,100000):
    is_prime_v2(n)
t1 = time.time()
print("Time required: ", t1-t0)
    
# Time required:  1.368093490600586

for n in range(1,100000):
    isPrime = is_prime_v1(n)
    if isPrime:  
        sys.stdout.write(BOLD + RED)
        print( n, isPrime)
        sys.stdout.write(RESET)        
    #else:
        #print(n, isPrime)

# Still imporvements can be made. We're checking even divisors
# for all odd numbers. This is a waste, since no odd number
# is divisable by an even number.

def is_prime_v3(n):
    """Return 'True' if 'n' is a prime number. False otherwise."""
    if n == 1:
        return False
    if n == 2:
        return True
    if n > 2 and n%2==0:
       return False
    else:
       for d in range(3,int(math.sqrt(n)),2):
           if n%d == 0:
               return False
    return True

# Test


for n in range(1,21):
    isPrime = is_prime_v3(n)
    if isPrime:  
        sys.stdout.write(BOLD + RED)
        print( n, isPrime)
        sys.stdout.write(RESET)      
    else:
        print(n, isPrime)
        
# And time it
t0 = time.time()
for n in range(1,100000):
    is_prime_v3(n)
t1 = time.time()
print("Time required: ", t1-t0)
    
# Time required:  0.7529726028442383


       
        
  
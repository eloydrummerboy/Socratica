# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Prime Numbers

# Write a function to compute 3x+1

def f(x):
    return 3*x+1
    
f(2)


# lambda method
lambda x: 3*x + 1

# However, this can't be used now, without a name
# So give it a name, and we're back to our original 
# fuction, but in one line of code
g = lambda x: 3*x + 1
g(2)


# Use case: Combine First and Last Names into single full name

full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()

# Test
full_name("   scOtt","   ADAMS   ")

# Lambda syntax
# lambda x1, x2, ..., xn : <expression>
# The result of <expression> is the return value
# exanples
lambda x,y: (x*y)**0.5 # Geometric Mean
lambda x,y,z: 3/(1/x + 1/y + 1/z) # Harmonic Mean

scifi_authors = ["Isaac Asimov", "Ray Bradbury", "Robert Heinlein",
                 "Arthur C. Clarke", "Frank Herbert", "Orson Scott Card", 
                 "Douglas Adams", "H. G. Wells", "Leigh Brackett"]
 # Want to sort by last name
 # We can use the included sort() function for lists, along
 # with the 'key' option
help(scifi_authors.sort)                 
scifi_authors.sort(key=lambda name: name.split(" ")[-1].lower())
print(scifi_authors)
      

# Suppose you're working with quadratic equations

def build_quadratic_function(a,b,c):
    """Returns the function f(x) = ax^2 + bx +c"""
    return lambda x: a*x**2 + b*x + c
    
f = build_quadratic_function(2,3,-5)
print(f(0))
print(f(1))
print(f(2))

build_quadratic_function(3,0,1)(2) # creates anonymous function 3x^2+1 evaluated at x=2




           
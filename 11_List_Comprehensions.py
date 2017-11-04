# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 07:14:32 2017

@author: eloy
"""

# List Comprehensions

# [expr for val in collection]
# [expr for val in collection if <test>]
# [expr for val in collection if <test1> and <test2]
# [expr for val1 in collection1 and val2 in collection2]


# List of squares of first 100 positive ints
# First, do without List Comprehensions

squares = []
for i in range(1,101):
    squares.append(i**2)
    
print(squares)


squares2 = [i**2 for i in range(1,101)]
print(squares2)


remainders5 = [x**2 % 5 for x in range(1,101)]
print(remainders5)

remainders11 = [x**2 % 11 for x in range(1,101)]
print(remainders11)

movies = ["Star Wars", "Gandhi", "Casablanca",
          "Shawshank Redemption", "Gone with the Wind",
          "Gattaca", "Rear Window", "Ghostbusters",
          "To Kill A Mockingbird", "Groundhog Day"]
# Find those movies that start with 'G'
gmovies = []
for title in movies:
    if title.startswith("G"):
        gmovies.append(title)
        
print(gmovies)

gmovies2 = [title for title in movies if title.startswith("G")]
print(gmovies2)

movies = [("Star Wars" , 1900), ("Gandhi", 1901), ("Casablanca",1903),
          ("Shawshank Redemption",1904), ("Gone with the Wind",1905),
          ("Gattaca",1906), ("Rear Window",1907), ("Ghostbusters",1908),
          ("To Kill A Mockingbird",1909), ("Groundhog Day", 1910)]

# Find all movies released before a certain date

newmovies = [(title,date) for (title,date) in movies if date > 1904]
print(newmovies)



# Scalar multiplication
v = [2,-3,1]
# We want 4 x v, so try
print(4*v)
print("-=-=-=-=-=-=-=-")
# This is not right, what we get is
# 4*v = v + v + v + v
# Adding lists = Concatenation
# Try, instead
ans = [4*x for x in v]
print(ans)

# Use List Comprehensions to compute the Cartesian Product
# If A and B are sets, then the Cartesian Product is the
# set of all possible pairs (a,b) where 'a' is in A and 
#'b' is in B.
# Mathematically: AxB = {a,b) | a∈A, b∈B}

A = {1,3,5,7}
B = {'x','y'}
cart_prod = [(a,b) for a in A  for b in B]

print(cart_prod)


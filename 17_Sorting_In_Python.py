# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 16:52:49 2017

@author: eloy
"""

# Sorting in Python

# Sorthing alphabetically
# Alkaline earth metals
earth_metals = ["Beryllium", "Magnesium", "Calcium", "Strontium",
                "Barium", "Radium"]
                
earth_metals.sort()
print(earth_metals)
earth_metals.sort(reverse=True)
print(earth_metals)


# What if elemtns are in a tuple instead of a list?        
earth_metals = ("Beryllium", "Magnesium", "Calcium", "Strontium",
                "Barium", "Radium")

earth_metals.sort()
# Tuples are immutable objects!!

help(list.sort)
# Key is a function that will be used to determine which values
# you sort by

# name - radius km - density g/cm3 - avg. dist. from sun AUs)
planets = [
("Mercury",2440,5.43,0.395),
("Venus",6052,5.24,0.723),
("Earth",6378,5.52,1.000),
("Mars",3396,3.93,1.530),
("Jupiter",71492,1.33,5.210),
("Saturn",60268,0.69,9.551),
("Uranus",25559,1.27,19.213),
("Neptune",24764,1.64,30.070),
]

# Currently sorted by distance from sun
# lets sort by size, largest first

# We need a function to return the size, so we
# can then set that as our key, and sort by it
# We use a lambda expression
size = lambda planet: planet[1]

planets.sort(key=size, reverse = True)

print(planets)

# Now let's do least dense to most dense
density = lambda planet: planet[2]
planets.sort(key=density)
print(planets)

# Sort changes the base list. What if we want it to stay the same
# and create a copy? What if we want to sort a tuple?
# Answer: Use sorted()

help(sorted)

earth_metals = ["Beryllium", "Magnesium", "Calcium", "Strontium",
                "Barium", "Radium"]

sorted_earth_metals = sorted(earth_metals)
print(sorted_earth_metals)
print(earth_metals)

# Sorting Tuples
data = (7,2,5,6,1,3,9,10,4,8)

sorted_data = sorted(data)
print(sorted_data)
print("Note the type of the result is now a list, not a tuple")
print(type(sorted_data))
print(data)
print("But the original tuple is unchanged. Of course. It's immutable!")

# Remember, strings are iterable
sorted("Alphabetical")






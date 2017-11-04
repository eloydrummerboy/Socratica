# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 15:18:18 2017

@author: eloy
"""
#import os
#os.chdir("/home/eloy/Programming/Python_Socratica/")

import logging


# Create and configure logger
LOG_FORMAT = "%(levelname)s %(asctime)s  %(message)s"
logging.basicConfig(filename = "/home/eloy/Programming/Python_Socratica/Wooden.Log", 
                    level = logging.DEBUG,
                    format = LOG_FORMAT)
logger = logging.getLogger()


def quadratic_formula(a,b,c):
    """Return the solutions to the equation ax^2 + bx + c = 0"""
    import math    
    logger.info("quadratic_formula({0},{1},{2})".format(a,b,c))
    
    # Compute the distriminant
    logger.debug("# Compute the discriminant")
    disc = b**2 - 4*a*c
    
    # Compute the two roots
    logger.debug("# Compute the two roots.")
    root1 = (-b + math.sqrt(disc)) / (2*a)
    root2 = (-b - math.sqrt(disc)) / (2*a)

    logger.debug("# Return the roots")
    return (root1, root2)

print("Let's solve the quadratic equation:")
print(" a*x^2 + b*x + c = 0")
a = float(input("Enter a:"))
b = float(input("Enter b:"))
c = float(input("Enter c:"))

print(quadratic_formula(a,b,c))

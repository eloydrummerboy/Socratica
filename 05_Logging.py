# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 09:10:44 2017

@author: eloy
"""
#import os
#os.chdir("/home/eloy/Programming/Python_Socratica/")

import logging

# Create and configure logger
LOG_FORMAT = "%(levelname)s %(asctime)s  %(message)s"
logging.basicConfig(filename = "/home/eloy/Programming/Python_Socratica/Lumberjack.Log", 
                    level = logging.DEBUG,
                    format = LOG_FORMAT)
logger = logging.getLogger()

# Test the Logger
logger.info("Anybody home?")
logger.debug("Debugging the fuck out of this code!")
logger.error("Oh Shit! It's an Error")
logger.critical("I'm in your computer, making logs!!")

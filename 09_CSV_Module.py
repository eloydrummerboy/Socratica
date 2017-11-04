# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 22:13:52 2017

@author: eloy
"""

# CSV Module

# Data from https://goo.gl/3zaUlD
import os
os.chdir("./Programming/Python_Socratica/")

path = "./google_stock_data.csv"
file = open(path)

# Display data
for line in file:
    print(line)
    
# Another way, read contents of file using
# a list comprehension
lines = [line for line in open(path)]

# Print a particular line
lines[1]

# Notice the entire line is a string, and the trailing
# newline character


lines[0].strip().split(',')

# Now, do this inside the List Comprehension
# as you read the data in
dataset = [line.strip().split(',') for line in open(path)]

# now try using the csv module
import csv

print(dir(csv))

file = open(path, newline='')
reader = csv.reader(file)

header = next(reader) # the first line is the header
data = [row for row in reader] # Read the remaining data

print(header)
print(data[0])

# This is more lines of code, but also more robust
# The csv module takes care of many edge cases such as commas
# within a string value, etc.

# We still don't have our data in the correct type
# Date is datetime
# Open, High, Low, Close, Adj Close are Float
# Volue is Int

from datetime import datetime

file = open(path, newline='')
reader = csv.reader(file)

header = next(reader) # the first line is the header

data = []
for row in reader:
    date = datetime.strptime(row[0], '%m/%d/%Y')
    open_price = float(row[1]) #open in __builtin__ function
    high = float(row[2])
    low = float(row[3])
    close = float(row[4])
    volume = int(row[5])
    adj_close = float(row[6])
    
    data.append([date,open_price,high,low,close,volume,adj_close])
    
print(data[0])

# Compute daily stock returns
# Write to .csv
# Stock Return = % change in price

returns_path = "./google_returns.csv"
file = open(returns_path, 'w')
writer = csv.writer(file)

writer.writerow(["Date","Return"])

for i in range(len(data) -1):
    todays_row = data[i]
    todays_date = todays_row[0]
    todays_price = todays_row[-1]
    yesterdays_row = data[i+1]
    yesterdays_price = yesterdays_row[-1]
    
    daily_return = ((todays_price - yesterdays_price) / yesterdays_price)
    formatted_date = todays_date.strftime('%m/%d/%Y')    
    writer.writerow([formatted_date, daily_return])
    




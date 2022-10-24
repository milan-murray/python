"""
Milan Murray 27/09/2019
Week 2 Lab
"""

# 1.Convert 35 degrees Fahrenheit to degrees Celsius.
# We need a variable for both fahrenheit and celsius.
# The data type for both fahrenheit and celsius will be floating points.
# Containers can be made for constants in the formula.

fahrenheit = 100
CONVERSION_FACTOR = (5/9)
BASE = 32

celsius = (CONVERSION_FACTOR)*(fahrenheit - BASE)
celsius = round(celsius, 2)

print(fahrenheit, "degrees farhenheit is equal to", celsius, "degrees celsius.")

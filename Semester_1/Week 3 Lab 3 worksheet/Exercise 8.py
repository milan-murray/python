"""
Milan Murray 04/10/19
Exercise 8: Input the radius of a circle and print the area of that circle.
"""

# Constants
PI = 3.14159
POWER = 2

# Inputs
radius = float(input("Please enter a radius: "))

# Processing
area = radius * PI ** POWER
area = round(area, 3)

# Output
print("A circle with radius ", radius, "has an area of ", area, "units squared.")
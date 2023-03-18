"""
Milan Murray 25/10/19
Exercise 2: Develop a program that inputs a radius of a circle and outputs the area.
"""
# Other
import math

# Constants
SIGNIFICANT_FIGURES = 3
RADIUS_TO_BE_SQUARED = 2

# Inputs
radius = float(input("Please enter the radius of the circle: "))

# Processes
if radius > 0:
    area = math.pi * (radius ** RADIUS_TO_BE_SQUARED)
    area = round(area, SIGNIFICANT_FIGURES)
    radius_input = "Valid."
else:
    area = 0
    radius_input = "Invalid."

# Outputs
print("The radius value is", radius_input)
if radius_input == "Valid.":
    print("The area of a circle with radius", radius, "unit(s) is:", area, "unit(s) squared.")

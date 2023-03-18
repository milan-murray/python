"""
Milan Murray 27/09/2019
Week 2 Lab
"""

# We need to determine the area og grass on
# the yard by removing the area of the house from the yard.
# We can then determine the required time.

GRASS_CUT_TIME = 2

LENGTH_HOUSE = 60
WIDTH_HOUSE = 45

LENGTH_YARD = 80
WIDTH_YARD = 64

AREA_HOUSE = LENGTH_HOUSE*WIDTH_HOUSE
AREA_YARD = (LENGTH_YARD*WIDTH_YARD) - AREA_HOUSE

required_time = AREA_YARD / GRASS_CUT_TIME
required_time = round(required_time, 2)

print("The required time to cut the grass on the yard is: ", required_time, "seconds.")
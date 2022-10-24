"""
Milan Murray 25/10/19
Exercise 4: Develop a program that generates a random number and calculates the sum from 1 to that number.
"""
# Other
import random

# Constants
LOWER_THRESHOLD = 1
UPPER_THRESHOLD = 5

# Inputs

# Processes
random_number = random.randint(LOWER_THRESHOLD, UPPER_THRESHOLD)
counter = random_number
total_sum = 0

while counter >= 1:
    total_sum += counter
    counter -= 1

# Outputs
print("The total sum of numbers from 1 to", random_number, "is:", total_sum)

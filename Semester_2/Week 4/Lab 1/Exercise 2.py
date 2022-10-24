"""
Milan Murray X00162027 | 20-Feb-2020 | Thursday
Exercise 2:  Print a random number to the screen using a function
"""
# Imports
import random


# Definitions
def generate_print_rand():
    random_number = random.randint(0, 100)
    print("The random number is: ", random_number)


# Processes
for i in range(10):
    generate_print_rand()

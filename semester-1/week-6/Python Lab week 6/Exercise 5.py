"""
Milan Murray 25/10/19
Exercise 5: Develop a program that loops the numbers from 1 to 20 and states if the number is even or odd.
"""
# Other

# Constants
MAX_NUMBER = 20
DIVIDER = 2

# Other

# Inputs

# Processes & Output
number = 1
while number <= MAX_NUMBER:
    if not number % DIVIDER:
        even_odd = "even."
    else:
        even_odd = "odd."
    print(number, "- This number is", even_odd)
    number += 1

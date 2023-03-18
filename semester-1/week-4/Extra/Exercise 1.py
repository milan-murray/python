"""
Milan Murray 13/10/19
Exercise 1: Input and int and output even or odd
"""
# Constants
DIVISOR = 2
PROOF = 0

# Inputs
user_number = int(input("Please enter a whole number: "))

# Processes
if user_number % DIVISOR == PROOF:
    even_odd_check = "even."
else:
    even_odd_check = "odd."

# Outputs
print("\nThe number you have entered is", even_odd_check)
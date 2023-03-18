"""
Milan Murray 13/10/19
Exercise 2: Design and develop a program that determines the purchasing policy to be followed by employees
"""

# Constants
UPPER_PRICE_THRESHOLD = 5000
LOWER_PRICE_THRESHOLD = 500

# Inputs
price = int(input("Please enter the price of your purchase: "))

# Processes
if price > UPPER_PRICE_THRESHOLD:
    instructions = "Please go to tender."
elif price >= LOWER_PRICE_THRESHOLD:
    instructions = "Quotes from 3 unique tenders are required."
else:
    instructions = "You may proceed with the purchase."

# Outputs
print(instructions)
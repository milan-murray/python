"""
Milan Murray 08/10/19
Sample if question.
"""

# Inputs
hours_worked = int(input("How many hours have you worked?: "))
rate = int(input("At what rate?: "))

# Constants
BONUS_TOTAL = rate + (rate * 0.5)

# Processing
pay = rate * hours_worked
if hours_worked > 40:
    pay = pay + ((hours_worked - 40) * (rate * 0.5))

# Output
print("You have earned: ", pay, "euro.")
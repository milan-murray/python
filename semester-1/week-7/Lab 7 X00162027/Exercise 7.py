"""
Milan Murray 08/11/2019
Exercise 7: Determine if an inputted year is a leap year or not.
"""
print("\n---\tExercise 7: Determine if an inputted year is a leap year or not.\t---\n")
# Other

# Constants
LEAP_DIVISOR_RULE_1 = 4
LEAP_DIVISOR_RULE_2 = 100
LEAP_DIVISOR_RULE_3 = 400

# Inputs
year = int(input("Please enter a year: "))

# Processes
if year % LEAP_DIVISOR_RULE_1 == 0:
    if year % LEAP_DIVISOR_RULE_2 != 0:
        leap_year = True    # If divisible by 4 & not divisible by 100: True
    else:
        if year % LEAP_DIVISOR_RULE_3 == 0:
            leap_year = True    # If divisible by 4 & divisible by 100 & divisible by 400: True
        else:
            leap_year = False   # If divisible by 4 & not divisible by 100 & divisible by 400: False
else:
    leap_year = False   # If not divisible by 4: False

# Outputs
print("The year you have entered is:", year)
print("Leap year:", leap_year)

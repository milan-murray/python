"""
Milan Murray ¦ 09-Jan-2020 ¦ Thursday
Exercise 1: Input name and age from user, output when the user will be 100 years old.
"""
# Imports

# Other

# Constants
YEAR_CHECK = 100

# Inputs
user_name = input("Please enter your first name: ")
user_age = int(input("Please enter your age: "))

# Processes & Outputs
if user_age < YEAR_CHECK:
    years_from_one_hundred = YEAR_CHECK - user_age
    print("Hello", user_name + ", you will be 100 years old in", years_from_one_hundred, "years.")
elif user_age == YEAR_CHECK:
    print("Congratulations", user_name + "! You are 100 years old.")
else:
    years_from_one_hundred = user_age - YEAR_CHECK
    print("Hello", user_name + ", you are", years_from_one_hundred, "years older than 100.")

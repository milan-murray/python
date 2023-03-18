"""
Milan Murray 25/10/19
Exercise 1: Develop a program that inputs a date of birth and outputs the current age of the user.
"""
# Other
import time
current_year = int(time.strftime("%Y"))
current_month = int(time.strftime("%m"))
current_day = int(time.strftime("%d"))

# Constants
LAST_CHAR_YEAR = 10
FIRST_CHAR_YEAR = 6
LAST_CHAR_MONTH = 5
FIRST_CHAR_MONTH = 3
LAST_CHAR_DAY = 2
FIRST_CHAR_DAY = 0
FORMAT_CHARS = 10

# Inputs
dob = input("Please enter you date of birth in the format DD/MM/YYYY: ")

# Processes
dob_year = int(dob[FIRST_CHAR_YEAR:LAST_CHAR_YEAR])
dob_month = int(dob[FIRST_CHAR_MONTH:LAST_CHAR_MONTH])
dob_day = int(dob[FIRST_CHAR_DAY:LAST_CHAR_DAY])

if len(dob) != FORMAT_CHARS:
    user_age = "Incorrect date of birth format."
else:
    user_age = (current_year - dob_year) - 1
    if current_month > dob_month:
        user_age += 1
    elif current_month == dob_month and current_day > dob_day:
        user_age += 1

# Outputs
print("Age:", str(user_age))

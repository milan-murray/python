"""
Milan Murray 04/10/19
Exercise 6: Take an input from the user and create a new string based on multiples of the original string.
"""
# Constants

# Inputs
user_input = input("Please enter a string: ")
user_number = int(input("Please enter a number: "))

# Processing
new_string = "\"" + (user_input + " ") * (user_number - 1) + user_input + "\""

# Outputs
print("The newly created string is: ", new_string, end="")
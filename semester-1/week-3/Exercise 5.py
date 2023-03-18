"""
Milan Murray 04/10/19
Exercise 5: Print first and last 2 characters from an input of 4 or more characters.
"""
# Constants

# Inputs
user_input = input("Please enter a word which contains at least 4 characters: ")

# Processing
first_character = user_input[0]
second_character = user_input[1]
second_last_character = user_input[-2]
last_character = user_input[-1]
new_word = first_character + second_character + second_last_character + last_character

# Output
print(user_input, "is the word you have entered.")
print(new_word, "is the new generated word.")
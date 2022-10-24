"""
Milan Murray 08/11/2019
Exercise 5: Calculate the number of commas in a string to be inputted by the user.
"""
print("\n---\tExercise 5: Calculate the number of commas in a string to be inputted by the user.\t---\n")
# Other
current_comma_location = 0
comma_counter = 0

# Constants

# Inputs
users_word = input("Please enter a sentence with commas: ")
length_of_string = len(users_word)
remainder_of_word = users_word[0:]

# Processes
while "," in remainder_of_word:
    # print(remainder_of_word)  # Useful to visualise the logic.
    comma_counter += 1
    current_comma_location = remainder_of_word.index(",")
    remainder_of_word = remainder_of_word[(current_comma_location + 1):]

# Outputs
if length_of_string == 1:
    print("Your sentence has", length_of_string, "character.")
else:
    print("Your sentence has", length_of_string, "characters.")
if comma_counter == 1:
    print("There is", comma_counter, "comma in the entered text.")
else:
    print("There are", comma_counter, "commas in the entered text.")

"""
Milan Murray X00162027 | 13-Feb-2020 | Thursday
Exercise 2:  Search for names in a text file and add a new name if it is not already there
"""
# Constants
MIN_NAME_CHARS = 10

# Inputs & Processes
with open("names.txt", "r") as r_text_file:
    name_text = r_text_file.read()
name_list = name_text.split("\n")

search_name = input("Please enter a name to search for in the file: ")
while len(search_name) < MIN_NAME_CHARS:
    search_name = input("Invalid name, please enter a name with more than 10 characters: ")

if search_name in name_list:
    print("The name", search_name, "was in the text file.")
else:
    user_choice = input("Name not in file. Would you like to add it? Y/N: ")
    if user_choice == "y" or user_choice == "Y":
        with open("names.txt", "a") as a_text_file:
            a_text_file.write(search_name)
        print("Name added to text document.")
    else:
        print("No changes made.")

"""
Milan Murray X00162027 | 13-Feb-2020 | Thursday
Exercise 1:  Take in 5 user's names and add them to a plain text document
"""
# Constants
MIN_NAME_CHARS = 10

# Inputs & processes
with open("names.txt", "w") as text_file:
    for i in range(5):
        print("Name", str(i + 1), "\n¬¬¬¬¬¬¬¬¬¬¬¬")
        name = input("Please enter a name: ")
        while len(name) < MIN_NAME_CHARS:
            name = input("Please enter a name with more than 10 characters: ")
        text_file.write(name + "\n")
        print()

with open("names.txt", "r") as text_file:
    read_file = text_file.read()

# Outputs
print(read_file)

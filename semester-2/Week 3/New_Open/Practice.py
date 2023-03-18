"""
Milan Murray X00162027 | 11-Feb-2020 | Tuesday
Exercise 1:  Practice open()
"""
# Imports

# Other
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
vowel_counter = 0
space_counter = 0

# Constants

# Inputs

# Processes & Outputs
my_file = open("my_text.txt", "r")
all_text = my_file.read()
my_file.close()

print(all_text)

for character in all_text:
    if character == " ":
        space_counter += 1
    elif character in vowels:
        vowel_counter += 1

print("Vowels:", vowel_counter)
print("Spaces:", space_counter)


my_file = open("my_text.txt", "r")
all_text = my_file.readlines()
for line in all_text:
    input("Press enter to continue...")
    print(line)

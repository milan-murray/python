"""
Milan Murray 23/11/19
Exercise 4: Verify if a phrase is a palindrome
"""
# Other
reverse = ""
original_no_space = ""

# Constants


# Inputs
phrase_check = input("Please enter \"Y\" or \"y\" if you wish to enter a phrase and check if it is a palindrome: ")

# Processes
while phrase_check == "Y" or phrase_check == "y":
    original = input("Please enter a phrase: ")
    original = original.upper()
    for i in range(len(original)):
        if original[i] != " ":
            original_no_space += original[i]
    for letter in range(len(original_no_space)-1, -1, -1):
        reverse += original_no_space[letter]
    if original_no_space == reverse:
        palindrome = True
    else:
        palindrome = False
    original_no_space = ""
    reverse = ""
    print("Palindrome validation:", palindrome)
    print()
    phrase_check = input("Enter \"Y\" or\"y\" to enter another phrase, else enter a different value: ")
# Outputs

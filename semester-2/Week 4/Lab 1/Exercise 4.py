"""
Milan Murray X00162027 | 20-Feb-2020 | Thursday
Exercise 4:  Use a function to print the longer of 2 strings.
"""


# Definitions
def print_longest_string(string1_in, string2_in):
    if len(string1_in) > len(string2_in):
        print("The longer word is: ", string1_in)
    elif len(string2_in) > len(string1_in):
        print("The longer word is: ", string2_in)
    else:
        print("The length of the words are even.")


# Inputs
string1 = input("Please enter a word: ")
string2 = input("Please enter another word: ")

# Processes
print_longest_string(string1, string2)

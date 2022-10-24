"""
Milan Murray 25/10/19
Exercise 6: Develop a program that creates a acronym from three words to be input.
"""
# Other
initials = ""

# Constants

# Inputs
three_words = input("Please enter three (or more) words separated by a space: ")


# Processes
"""
space_loc = three_words.index(" ")
last_two_words = three_words[(space_loc+1):]

space_loc = last_two_words.index(" ")
last_word = last_two_words[(space_loc + 1):]

initial_1 = three_words[0]
initial_2 = last_two_words[0]
initial_3 = last_word[0]

initial_1 = initial_1.upper()
initial_2 = initial_2.upper()
initial_3 = initial_3.upper()
"""
remainder_sentence = three_words.upper()

while " " in remainder_sentence:
    initials += remainder_sentence[0]
    space_loc = remainder_sentence.index(" ")
    remainder_sentence = remainder_sentence[(space_loc + 1):]
initials += remainder_sentence[0]   # For the final initial

# Outputs
print("The three letter acronym for these words are:", initials)

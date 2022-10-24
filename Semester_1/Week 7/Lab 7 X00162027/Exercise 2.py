"""
Milan Murray 08/11/2019
Exercise 2: Allow the user to input 5 floating point numbers using a for loop, print the average.
"""
print("\n---\tExercise 2: Allow the user to input 5 floating point numbers using a for loop, print the average.\t---\n")
# Other
sum_numbers = 0

# Constants
AMOUNT_OF_NUMBERS = 5
SIGNIFICANT_FIGURES = 2

# Inputs

# Processes
for counter in range(0, AMOUNT_OF_NUMBERS):
    number = float(input("Please enter a number: "))
    sum_numbers += number

average_of_numbers = sum_numbers / AMOUNT_OF_NUMBERS
average_of_numbers = round(average_of_numbers, SIGNIFICANT_FIGURES)

# Outputs
print("The average of these numbers are:", average_of_numbers)

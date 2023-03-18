"""
Milan Murray X00162027 | 20-Feb-2020 | Thursday
Exercise 3:  Print all the numbers from 0 to an inputted number that is odd.
"""


# Definitions
def print_odd_nums(threshold_in):
    for number in range(0, threshold_in + 1):
        if number % 2 != 0:
            print(number)


# Inputs
threshold = int(input("Please enter the upper threshold: "))

# Processes & outputs
print_odd_nums(threshold)

"""
Milan Murray ¦ 15-Jan-2020 ¦ Wednesday
Exercise : Fill a list with random int numbers and make a bubble sort the list.
"""
# Imports
import random

# Other
number_list = []
sort_check = 1

# Constants
RAND_THRESHOLD_MIN = -200
RAND_THRESHOLD_MAX = 200
AMOUNT_NUMS_IN_LIST = 7

# Processes - fill the list with random ints
for i in range(AMOUNT_NUMS_IN_LIST):
    number_list.append(random.randint(RAND_THRESHOLD_MIN, RAND_THRESHOLD_MAX))

# Output unsorted list
print(number_list)

# Processes - Bubble sort the list
input("Press enter to begin the sorting process...")
while sort_check != 0:  # LCV
    sort_check = 0
    for value in range(AMOUNT_NUMS_IN_LIST - 1):
        if number_list[value] > number_list[value + 1]:     # If the next number is smaller
            print(number_list)
            sort_check = 1
            smaller_num = number_list[value + 1]  # Store the smaller number in another variable
            number_list[value + 1] = number_list[value]     # Replace the small number with the big number
            number_list[value] = smaller_num

print("\nThe sorted list is:", number_list)

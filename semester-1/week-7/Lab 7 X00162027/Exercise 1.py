"""
Milan Murray 08/11/2019
Exercise 1: Add the numbers between 50 and 100 (inclusive) using while and for loops.
"""
print("\n---\tExercise 1: Add the numbers between 50 and 100 (inclusive) using while and for loops.\t---\n")
# Other
counter_while = 50
total_sum_while = 0
total_sum_for = 0

# Constants
THRESHOLD_HIGHER = 101
THRESHOLD_LOWER = 50

# Inputs

# Processes
while counter_while < THRESHOLD_HIGHER:
    total_sum_while += counter_while
    counter_while += 1

for counter_for in range(THRESHOLD_LOWER, THRESHOLD_HIGHER):
    total_sum_for += counter_for

# Outputs
print("The sum of numbers from 50 to 100 (inclusive) using a while loop:", total_sum_while)
print("The sum of numbers from 50 to 100 (inclusive) using a for loop:", total_sum_for)

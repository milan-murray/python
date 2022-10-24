"""
Milan Murray 08/11/2019
Exercise 6: Input a starting number, ending number & step for a counting program. Output each number and the sum.
"""
print("\n---\tExercise 6: Input a starting number, ending number & step for a counting program.\t---\n")
# Other
sum_of_counter = 0

# Constants

# Inputs
start_number = int(input("Please enter the starting number: "))
ending_number = int(input("Please enter the ending number (inclusive): "))
step = int(input("Please enter the step the counter should take: "))

# Processes
ending_number += 1

for counter in range(start_number, ending_number, step):
    print(counter)
    sum_of_counter += counter

# Outputs
print("The sum of these numbers is:", sum_of_counter)

"""
Milan Murray 08/11/2019
Exercise 3: Add all the even and odd numbers between 1 and 20 separately. Print the results of both.
"""
print("\n---\tExercise 3: Add all the even and odd numbers between 1 and 20 separately. "
      "Print the results of both.\t---\n")
# Other
counter = 0
even_sum = 0
odd_sum = 0

# Constants

# Inputs

# Processes
for counter in range(1, 21):
    if counter % 2 == 0:
        even_sum += counter
    else:
        odd_sum += counter

# Outputs
print("The sum of the even numbers between 1 and 20 are:", even_sum)
print("The sum of the odd numbers between 1 and 20 are:", odd_sum)

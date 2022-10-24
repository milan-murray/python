"""
Milan Murray 22/11/19
Exercise X: Make a program that prints a template for Python
"""
# Other
import time

start_end_mark = "¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬ ¬"
structure = "# Other\n\n\n" \
            "# Constants\n\n\n" \
            "# Inputs\n\n\n" \
            "# Processes\n\n\n" \
            "# Outputs\n\n\n"

# Constants


# Inputs
exercise_number = input("Please enter the exercise number: ")
exercise_description = input("Please enter the description of the task (Enter 0 for blank description): ")
print()

# Processes
print(start_end_mark)
print(time.strftime("\"\"\"\nMilan Murray %d/%m/%y"))
print("Exercise", str(exercise_number) + ": ", end="")
if exercise_description != "0":
    print(exercise_description, "\n\"\"\"")
else:
    print("\n\"\"\"")
print(structure)
print(start_end_mark)
# Outputs


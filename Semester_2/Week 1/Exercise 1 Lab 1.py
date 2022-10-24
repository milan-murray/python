"""
Milan Murray ¦ 30-Jan-2020 ¦ Thursday
Exercise 1:  Read in 4 exam results from 5 students and calculate statistics based on that data.
"""
# Imports
from statistics import mean

# Other - Initialise lists and counters
total_result_list = []

equal_greater_counter = 0

# Constants
AMOUNT_OF_STUDENTS = 5
AMOUNT_OF_SUBJECTS = 4
MARK_THRESHOLD_LOWER = 0
MARK_THRESHOLD_HIGHER = 100

# Inputs - Input exam results from user using a 'for' loop
for i in range(AMOUNT_OF_STUDENTS):
    student_result_list = []
    student = i + 1  # Used to identify the student during data input
    print("\nStudent:", student, "\n¬¬¬¬¬¬¬¬¬¬¬¬")

    for subject in range(AMOUNT_OF_SUBJECTS):
        print("Subject", subject + 1)
        result = int(input("Please enter the student's result: "))

        # Input validation for value of 'result'
        while result < MARK_THRESHOLD_LOWER or result > MARK_THRESHOLD_HIGHER:
            result = int(input("Please enter a valid result: "))

        student_result_list.append(result)  # Temporary list used to create 2D list 'total_result_list'
    # List of all the students results
    total_result_list.append(student_result_list)
print()

# Processes
# List of all the average results for each student
average_total_result_list = [round(mean(row), 2) for row in total_result_list]

overall_average = round(mean(average_total_result_list), 2)

for index, average_of_student in enumerate(average_total_result_list):  # Loop to compare average results to the overall
    if average_of_student > overall_average:
        distance_from_average = overall_average - average_of_student
        distance_from_average = round(distance_from_average, 2)
        equal_greater_counter += 1
        print("Congratulations student", str(index + 1) + "! Your average result of", str(average_of_student) +
              "/100 is greater than the overall average of", str(overall_average) + "/100.")
        print("Distance from overall average:", distance_from_average, "marks.")
        print()

    elif average_of_student == overall_average:
        equal_greater_counter += 1
        print("Student", index + 1, "has an average result equal to the overall average of", str(average_of_student) +
              "/100.")
        print()

    else:
        distance_from_average = overall_average - average_of_student
        distance_from_average = round(distance_from_average, 2)
        print("Student", index + 1, "has an average result of", str(average_of_student) + "/100 which is below the "
                                                                                          "overall average of",
              str(overall_average) + "/100.")
        print("Distance from overall average:", distance_from_average, "marks.")
        print()

print("The amount of students that scored equal to or greater than the overall average:", equal_greater_counter)
input("Press enter to continue..")
print("¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬\n")

# Max result for all subjects
for index in range(AMOUNT_OF_SUBJECTS):  # Create a loop to isolate values in the list
    temp_subject_results = [row[index] for row in total_result_list]  # Store subject results based on index

    temp_max = max(temp_subject_results)
    temp_student_max = (temp_subject_results.index(temp_max) + 1)

    print("Student", temp_student_max, end=" ")

    temp_subject_results.remove(temp_max)
    student_counter = 1  # Initialize a counter for additional students

    while temp_max in temp_subject_results:  # This loop will print additional students that met the max mark
        student_counter += 1  # Used to identify multiple winners
        print("and student", temp_subject_results.index(temp_max) + student_counter, end=" ")
        temp_subject_results.remove(temp_max)

    print("scored the highest mark in subject", index + 1, "of", str(temp_max) + "/100.")
print()

# Create a 1D list of the students total marks out of 400
sum_total_results = [sum(row) for row in total_result_list]
min_mark = min(sum_total_results)
min_mark_student = sum_total_results.index(min_mark)
print("The lowest total mark was", str(min_mark) + "/400 from student", str(min_mark_student) + ".\n")

sorted_sum_total_results = sorted(sum_total_results)
print("All of the total results out of 400, sorted from smallest to largest are as follows: ", end="")
for i in range(AMOUNT_OF_STUDENTS - 1):
    print(str(sorted_sum_total_results[i]) + ", ", end="")
print(sorted_sum_total_results[-1])


print("Exhale at redundancy", end="\n")

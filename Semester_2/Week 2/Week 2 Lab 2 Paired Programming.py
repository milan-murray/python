"""
Milan Murray(X00162027) & Nikola Maj(X00162241) | 07-Feb-2020 | Friday
Exercise 1:  Hourly rate of employee's skill in a 2D List
"""
# Imports
from statistics import mean

# Other
pay_rates = [[10.5, 12.0, 14.5, 16.75, 18.0], [20.5, 22.25, 24.0, 26.25, 28.0],
             [34.0, 36.5, 38.0, 40.35, 43.0], [50.0, 60.0, 70.0, 80.0, 99.99]]

# Constants

# Processes
# Question 1
grade_three_pay_list = [step for step in pay_rates[2]]
average_pay_grade_three = mean(grade_three_pay_list)
print("Question 1:\n¬¬¬¬¬¬¬¬¬¬¬¬")
print("The mean pay for grade 3 is:", average_pay_grade_three)
input("Press enter to continue..")
print()

# Question 2
print("Question 2:\n¬¬¬¬¬¬¬¬¬¬¬¬")
for index, row in enumerate(pay_rates):
    temp_avg = mean(row)
    grade_no = index + 1
    print("The average for grade", grade_no, "is:", temp_avg)
input("Press enter to continue..")
print()

# Question 3
print("Question 3\n¬¬¬¬¬¬¬¬¬¬¬¬")
for index, row in enumerate(pay_rates):
    max_grade = max(row)
    min_grade = min(row)
    difference_grade = max_grade - min_grade
    difference_grade = round(difference_grade, 2)
    print("The difference for step", index + 1, "is:", difference_grade)
input("Press enter to continue..")
print()

# Question 4
print("Question 4\n¬¬¬¬¬¬¬¬¬¬¬¬")
print("\t\t{0:^90}".format("Payscale Tables"))
print("\t\t{0:^20}{1:^20}{2:^20}{3:^20}{4:^20}".format("Step 1", "Step 2", "Step 3", "Step 4", "Step 5"))
print("_" * 110)
for index, row in enumerate(pay_rates):
    grade = index + 1
    print("Grade :" + str(index + 1), end="")
    for col in row:
        print("{0:^20}".format(col), end="")
    print()
input("Press enter to continue..")
print()

# Question 5
print("Question 5\n¬¬¬¬¬¬¬¬¬¬¬¬")
for row in range(len(pay_rates)):
    for col in range(len(pay_rates[row])):
        pay_rates[row][col] += 1.5
print("Table updated.")
input("Press enter to continue..")
print()

# Question 6
print("Question 6\n¬¬¬¬¬¬¬¬¬¬¬¬")
print("\t\t{0:^90}".format("Payscale Tables -Updated"))
print("\t\t{0:^20}{1:^20}{2:^20}{3:^20}{4:^20}".format("Step 1", "Step 2", "Step 3", "Step 4", "Step 5"))
print("_" * 110)
for index, row in enumerate(pay_rates):
    grade = index + 1
    print("Grade :" + str(index + 1), end="")
    for col in row:
        print("{0:^20}".format(col), end="")
    print()
input("Press enter to continue..")
print()

# Outputs


"""
Milan Murray X00162027 | 20-Feb-2020 | Thursday
Exercise 1:  Pima-indians data set
"""
# Imports
import csv

# Other
bl_pr_results_total = 0
counter = 0

# Processes
with open("pima.csv") as pima_file:
    pima_data_list = list(csv.reader(pima_file))

for row in pima_data_list:
    for index, col in enumerate(row):
        if index == 2:
            if int(col) != 0:
                bl_pr_results_total += int(col)
                counter += 1
average_blood_pressure = bl_pr_results_total // counter

for index1, row in enumerate(pima_data_list):
    for index2, col in enumerate(row):
        if index2 == 2:
            if int(col) == 0:
                pima_data_list[index1][index2] = average_blood_pressure

with open("pima_new.csv", "w") as pima_new_file:
    write = csv.writer(pima_new_file)
    write.writerows(pima_data_list)

"""
Milan Murray X00162027 | 13-Feb-2020 | Thursday
Exercise 3:  Read in data from 10 people and display the max and min ages
"""
# Optional imports
from statistics import mean

# Other
separated_data_list = []
age_list = []

min_age = 120
max_age = 0

total_sum_ages = 0

# Constants
AGE_COL = 2

# Inputs & Processes
with open("population2.txt", "r") as num_file:
    num_text = num_file.read()
data_list = num_text.split("\n")  # Isolate the data per person in a 1D list

for data in data_list:
    separated_data = data.split(" ")
    separated_data_list.append(separated_data)  # Isolate the data per person in a 2D list
separated_data_list.remove(separated_data_list[-1])  # Remove the empty list at the end due to the extra "\n"
print(separated_data_list)

for data in separated_data_list:
    age_list.append(int(data[AGE_COL]))
print(age_list)

for age in age_list:
    if age > max_age:
        max_age = age
    elif age < min_age:
        min_age = age
    total_sum_ages += age

average_age = total_sum_ages / len(age_list)

# Alternate method of finding the min/max/avg
"""
average_age = mean(age_list)
max_age = max(age_list)
min_age = min(age_list)
"""

# Outputs
print("Minimum age:", min_age)
print("Maximum age:", max_age)
print("Average age:", average_age)

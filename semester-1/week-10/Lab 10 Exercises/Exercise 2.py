"""
Milan Murray 29/11/19
Exercise 2: Track hours worked of college department
"""
# Other
total_hours_worked = 0
hours_per_day_list = []
days_list = ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5"]
days_over_six_hours = 0

# Constants
WORKING_DAYS = 5
MIN_WORKING_HOURS = 0
MAX_WORKING_HOURS = 9
OVER_SIX_HOURS = 6
SIGNIFICANT_FIGURE = 2

# Processes
for value in range(WORKING_DAYS):
    hours = int(input("Please enter the amount of hours worked: "))
    while hours < MIN_WORKING_HOURS or hours > MAX_WORKING_HOURS:
        hours = int(input("Please enter a valid amount of hours: "))
    if hours > OVER_SIX_HOURS:
        days_over_six_hours += 1
    hours_per_day_list.append(hours)
    total_hours_worked += hours

average_hours_worked = total_hours_worked / WORKING_DAYS
average_hours_worked = round(average_hours_worked, SIGNIFICANT_FIGURE)

# Outputs
print("\nHours worked per day:")
for index in range(WORKING_DAYS):
    print(days_list[index] + ":", hours_per_day_list[index])
print("\nAverage hours worked:", average_hours_worked)
print("Total hours worked:", total_hours_worked)
print("Amount of days worked over 6 hours:", days_over_six_hours)

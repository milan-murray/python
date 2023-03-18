"""
Milan Murray ¦ 31-Jan-2020 ¦ Friday
Objective: ABC Ltd. Create a sales program to verify if employees reach a sales target
"""
# Imports

# Other
version_2_weekly_targets_list = []

all_employee_daily_sales = []
all_employee_sum_sales = []
exceeded_sales_counter = 0

# Constants
AMOUNT_OF_EMPLOYEES = 4
AMOUNT_OF_WEEKLY_FIGURES = 5

# """ Start of version 1

# Inputs & Processes
weekly_sales_target_figure = int(input("Please enter the weekly sales target figure: "))

for employee in range(AMOUNT_OF_EMPLOYEES):     # For each employee
    print("\nEmployee", employee + 1, "\n¬¬¬¬¬¬¬¬¬¬¬¬")
    temp_daily_sales = []   # Initialise & reset the list used to create a 2D list 'all_employee_daily_sales'

    for day in range(AMOUNT_OF_WEEKLY_FIGURES):    # For the amount of weekly sales
        print("Day", str(day + 1) + ": ", end="")
        daily_sale = int(input("Please enter the daily sales figure: "))
        temp_daily_sales.append(daily_sale)     # Take in each value and add it to the temp list
    all_employee_daily_sales.append(temp_daily_sales)   # Create the 2D list for all the sales figures
print()

# Processes
# Sum each employee's sales and store it in a list
all_employee_sum_sales = [sum(row) for row in all_employee_daily_sales]
total_sales = sum(all_employee_sum_sales)

for index in range(AMOUNT_OF_EMPLOYEES):
    print("Employee", str(index + 1) + "'s total sales figures are:", all_employee_sum_sales[index])

    if all_employee_sum_sales[index] > weekly_sales_target_figure:  # If the employee's sales exceed the weekly target
        exceeded_sales_counter += 1
        exceeded_amount = all_employee_sum_sales[index] - weekly_sales_target_figure    # Check by how much exceeded
        print("Employee", index + 1, "exceeded the weekly sales target by", exceeded_amount)

# Outputs
print("\nThe total amount of sales for the week:", total_sales)
print("Amount of employees that have exceeded the weekly target:", exceeded_sales_counter)

# End of version 1"""

""" Start of version 2

# Inputs & Processes
for employee in range(AMOUNT_OF_EMPLOYEES):
    print("\nEmployee", employee + 1, "\n¬¬¬¬¬¬¬¬¬¬¬¬")
    temp_sales_target = int(input("Please enter the sales target for this employee: "))
    version_2_weekly_targets_list.append(temp_sales_target)
print("\n¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬")

for employee in range(AMOUNT_OF_EMPLOYEES):     # For each employee
    print("\nEmployee", employee + 1, "\n¬¬¬¬¬¬¬¬¬¬¬¬")
    temp_daily_sales = []   # Initialise & reset the list used to create a 2D list 'all_employee_daily_sales'

    for day in range(AMOUNT_OF_WEEKLY_FIGURES):    # For the amount of weekly sales
        print("Day", str(day + 1) + ": ", end="")
        daily_sale = int(input("Please enter the daily sales figure: "))
        temp_daily_sales.append(daily_sale)     # Take in each value and add it to the temp list
    all_employee_daily_sales.append(temp_daily_sales)   # Create the 2D list for all the sales figures
print()

# Processes
# Sum each employee's sales and store it in a list
all_employee_sum_sales = [sum(row) for row in all_employee_daily_sales]
total_sales = sum(all_employee_sum_sales)

for index, col in enumerate(all_employee_sum_sales):
    print("Employee", str(index + 1) + "'s total sales figures are:", col)

    # If the employee's sales exceed the unique weekly target given to them
    if col > version_2_weekly_targets_list[index]:
        exceeded_sales_counter += 1
        exceeded_amount = col - version_2_weekly_targets_list[index]    # Check by how much exceeded
        print("Employee", index + 1, "exceeded their weekly sales target of", version_2_weekly_targets_list[index],
              "sales by", exceeded_amount)

# Outputs
print("\nThe total amount of sales for the week:", total_sales)
print("Amount of employees that have exceeded the weekly target:", exceeded_sales_counter)

End of version 2"""

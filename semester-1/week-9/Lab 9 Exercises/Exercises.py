"""
Milan Murray 22/11/19
Exercise 1: Input rainfall over a 7 day period, output total rainfall and average rainfall
"""
# Other
rainfall = []
total_rainfall = 0
days_excess_rain = ""

# Constants
DAYS_OF_WEEK = 7
SIGNIFICANT_FIGURE = 2
EXCESS_RAIN = 3.5

# Inputs


# Processes
for day in range(DAYS_OF_WEEK):
    print("Please enter the amount of rainfall(cm) for day", day + 1, end="")
    rainfall.append(float(input(": ")))
    total_rainfall += rainfall[day]

average_rainfall = total_rainfall / DAYS_OF_WEEK
average_rainfall = round(average_rainfall, SIGNIFICANT_FIGURE)

for day in range(DAYS_OF_WEEK):
    if rainfall[day] > EXCESS_RAIN:
        print("Rainfall exceeded 3.5cm on day", day + 1)

# Outputs
print("\nThe total rainfall for the week was:", str(total_rainfall) + "cm.")
print("The average rainfall for the week was", str(average_rainfall) + "cm.")
input("Press enter to continue...")
print()


"""
Milan Murray 22/11/19
Exercise 2: Write an application that initializes a list with 10 integer values and use the values for various tasks
"""
# Other
number_list = []
even_i = ""
even_num = ""
reverse_number_list = ""

# Constants


# Inputs


# Processes
for value in range(10, 101, 10):
    number_list.append(value)

# A
for i in range(len(number_list)):
    if i % 2 == 0:
        even_i += str(number_list[i]) + " "
print("The values at an even index of the number list are:", even_i)
print()

# B
for value in number_list:
    if value % 2 == 0:
        even_num += str(value) + " "
print("The even values of the list are: ", even_num)
print()

# C
print("The reverse of the list is: ", end="")
for value in range(9, -1, -1):
    print(number_list[value], "", end="")
print("\n")

# D
number_list.insert(1, int(input("Please enter a number to be inserted into the second index of the list: ")))
print()

# E
print(number_list)
print()

# F
print("Remove 30 from the list:")
if 30 in number_list:
    number_list.remove(30)
print(number_list)
print()


"""
Milan Murray 22/11/19
Exercise 3: Analyse sales person of a company
"""
# Other
sale_amount = []
total_sales = 0

# Constants


# Inputs
amount_of_salespeople = int(input("Please enter the number of sales people: "))

# Processes
for value in range(amount_of_salespeople):
    sale_amount.append(float(input("Please enter sales amount: ")))
max_value = sale_amount[0]
min_value = sale_amount[0]

print("\nSales Person\t\t\tSales €\n--------------------------------")
for value in range(amount_of_salespeople):
    print("Sales person", value + 1, "\t\t\t", sale_amount[value])
    total_sales += sale_amount[value]
    if sale_amount[value] > max_value:
        max_value = sale_amount[value]
    if sale_amount[value] < min_value:
        min_value = sale_amount[value]

average_sales = total_sales / amount_of_salespeople
average_sales = round(average_sales, 2)
input("Press enter to continue...")

# Outputs
print("\n¬¬¬\t\tSummary\t\t¬¬¬")
print("Total sales: €" + str(total_sales))
print("Average sales: €" + str(average_sales))
print("Maximum sale: €" + str(max_value))
print("Minimum sale: €" + str(min_value))


"""
Milan Murray 23/11/19
Exercise 4: Verify if a phrase is a palindrome
"""
# Other
reverse = ""
original_no_space = ""

# Constants


# Inputs
phrase_check = input("Please enter \"Y\" or \"y\" if you wish to enter a phrase and check if it is a palindrome: ")

# Processes
while phrase_check == "Y" or phrase_check == "y":
    original = input("Please enter a phrase: ")
    original = original.upper()
    for i in range(len(original)):
        if original[i] != " ":
            original_no_space += original[i]
    for letter in range(len(original_no_space)-1, -1, -1):
        reverse += original_no_space[letter]
    if original_no_space == reverse:
        palindrome = True
    else:
        palindrome = False
    original_no_space = ""
    reverse = ""
    print("Palindrome validation:", palindrome)
    print()
    phrase_check = input("Enter \"Y\" or\"y\" to enter another phrase, else enter a different value: ")
# Outputs

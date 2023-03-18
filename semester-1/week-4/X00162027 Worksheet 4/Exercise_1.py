"""
Milan Murray 11/10/19
Worksheet 4, Exercise 1: Design and develop a program that computes an employee’s income tax.
"""

# Constants
S_PERSON_TAX = 0.2
M_PERSON_TAX = 0.23
UNKNOWN_PERSON_TAX = 0
INCOME_THRESHOLD = 50000
TAX_ALLOWANCE_HIGH = 25000
TAX_ALLOWANCE_LOW = 20000

# Inputs
id_num = input("Please enter your identification number: ")
name = input("Please enter your name: ")
address = input("Please enter your address: ")
marital_status = input("Please indicate your marital status by entering S/M, for single or married: ")
gross_income = float(input("Please enter your gross pay: "))

# Processes
# Tax allowance
if gross_income < INCOME_THRESHOLD:
    tax_allowance = TAX_ALLOWANCE_HIGH
else:
    tax_allowance = TAX_ALLOWANCE_LOW
# Martial status & tax rate
if marital_status == "S":
    tax_rate = S_PERSON_TAX
    marital_check = "Single"
elif marital_status == "M":
    tax_rate = M_PERSON_TAX
    marital_check = "Married"
else:
    tax_rate = UNKNOWN_PERSON_TAX
    marital_check = "Unknown"

# Tax amount
tax = (gross_income - tax_allowance) * tax_rate

# Net income
net_income = gross_income - tax

# Outputs
print("Your name: ", name)
print("Your identification number is: ", id_num)
print("Your marital status: ", marital_check)
print("Gross income: ", gross_income)
print("Net pay: ", net_income)
print("Tax paid: ", tax)

password = input("\nPlease enter a password: ")
password_check = input("Please enter your password again: ")

if password == password_check:
    print("Password is correct.")
else:
    print("Passwords do not match.")
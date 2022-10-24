"""
Milan Murray 13/10/19
Exercise 3: Design and develop a program that calculates the motor
tax fee for a vehicle based on its engine size as input by the user
"""
# Constants
SIZE_THRESHOLD1 = 1000
SIZE_THRESHOLD2 = 1200
SIZE_THRESHOLD3 = 1400
SIZE_THRESHOLD4 = 1600
SIZE_THRESHOLD5 = 1800
SIZE_THRESHOLD6 = 2000
TAX1 = 150
TAX2 = 175
TAX3 = 200
TAX4 = 250
TAX5 = 300
TAX6 = 350
TAX_MAX = 500

# Inputs
engine_size = float(input("Please enter the size of your engine: "))

# Processes
if engine_size <= SIZE_THRESHOLD1:
    tax = TAX1
elif engine_size <= SIZE_THRESHOLD2:
    tax = TAX2
elif engine_size <= SIZE_THRESHOLD3:
    tax = TAX3
elif engine_size <= SIZE_THRESHOLD4:
    tax = TAX4
elif engine_size <= SIZE_THRESHOLD5:
    tax = TAX5
elif engine_size <= SIZE_THRESHOLD6:
    tax = TAX6
else:
    tax = TAX_MAX

# Outputs
print("The tax cost will be: ", tax)
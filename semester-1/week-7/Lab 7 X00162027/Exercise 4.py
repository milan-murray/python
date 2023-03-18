"""
Milan Murray 08/11/2019
Exercise 4: Currency conversion from Euro to Yen. Input rate and output equivalent Yen.
"""
print("\n---\tExercise 4: Currency conversion from Euro to Yen. Input rate and output equivalent Yen.\t---\n")
# Other

# Constants
CURRENCY_SIGNIFICANT_FIGURE = 2

# Inputs
currency_rate = float(input("Please enter the rate of yen to euro, enter \"0\" to stop: "))  # 120.77
if currency_rate != 0:
    euro = float(input("Please enter an amount of euro: "))

# Processes
    while euro != 0:
        yen = euro * currency_rate
        yen = round(yen, CURRENCY_SIGNIFICANT_FIGURE)
        print(euro, "euro equals", yen, "yen.")
        euro = float(input("Please enter an amount of euro, enter \"0\" to stop: "))
else:
    euro = 0

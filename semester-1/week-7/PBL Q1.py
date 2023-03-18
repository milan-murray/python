"""
Milan, Nikola & Tosin 07/11/2019
PBL Q1: College sleep
"""
# Other
counter = 0
total_sleep = 0

# Constants

# Inputs
house_name = input("Please enter the name of your house: ")
sleep_length = int(input("Please enter hours of sleep (0 to stop): "))

# Processes
if sleep_length != 0:
    while sleep_length != 0:
        counter += 1
        total_sleep += sleep_length
        sleep_length = int(input("Please enter hours of sleep (0 to stop): "))
    average_sleep = total_sleep / counter
    print("The total amount of inputs were: ", counter)
    print("The average amount of sleep was: ", average_sleep)
    print("The house is called: ", house_name)
else:
    print("Invalid entry")

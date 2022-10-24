"""
Milan Murray 21/11/19
GiftsToGo
"""
# Other
import random
loop_counter = 0

main_menu = "¦===============================¦\n" \
            "¦\t\t\tGiftsToGo\t\t\t¦\n" \
            "¦¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¦\n" \
            "¦\t1) Staff Pay\t\t\t\t¦\n" \
            "¦\t2) Company statistics\t\t¦\n" \
            "¦\t3) Generate Password\t\t¦\n" \
            "¦\t4) Exit\t\t\t\t\t\t¦\n" \
            "¦¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¦\n"

staff_menu = "¦===============================¦\n" \
             "¦\t\t\tStaff pay\t\t\t¦\n" \
             "¦¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¦\n"

# Constants

# Inputs
print(main_menu)
print()
option = int(input("Please select an option from the menu: "))
print()

# Processes
while option != 4:
    if loop_counter > 0:
        print(main_menu)
        print()
        option = int(input("Please select an option from the menu: "))
    while option < 1 or option > 4:
        option = int(input("Please enter a valid option: "))
    if option != 4:
        loop_counter += 1
        if option == 1:
            print(staff_menu)
            print()
            employee_name = input("Please enter employee name: ")

            for i in employee_name:
                pass


# Outputs


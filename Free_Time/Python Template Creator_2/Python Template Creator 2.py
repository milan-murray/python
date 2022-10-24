"""
Milan Murray X00162027 | 20-Feb-2020 | Thursday
Exercise 1:  Make Python Template Creator 2.0
"""
# Imports
import time


# Definitions
def main_menu_print():
    print("""
    ¦==================================================¦
    ¦{0:^30} Menu template:{1:^5}¦
    ¦--------------------------------------------------¦
    ¦\t1)\t{2:<27} Current: {3:<6}¦
    ¦\t2)\t{4:<43}¦
    ¦\t3)\t{5:<43}¦
    ¦\t4)\t{6:<43}¦
    ¦\t5)\t{7:<43}¦
    ¦==================================================¦
    """.format("Python Template Creator 2", menu_status, "Edit exercise number", exercise_number,
               "Edit exercise description", "Toggle menu template", "Print template", "Exit"))


def menu_head_print():
    print(time.strftime("\"\"\"\nMilan Murray X00162027 ¦ %d-%b-%Y ¦ %A"))


def exercise_head_print(exercise_number_in, desc_in):
    if exercise_number_in == "":
        print("Exercise:", end="")
    else:
        print("Exercise", str(exercise_number_in) + ": ", end="")
    print(desc_in, "\n\"\"\"")


def structure_print():
    print("# Imports\n\n\n# Definitions\n", end="")
    if toggle == 1:
        menu_template_print()
    print("\n\n# Other\n\n\n# Constants\n\n\n# Inputs\n\n\n# Processes\n\n\n# Outputs")


def menu_template_print():
    print("""def main_menu_print(): print(\"\"\"
    |==================================================|
    |{0:^50}|
    |--------------------------------------------------|
    | 1) {1:<46}|
    | 2) {2:<46}|
    | 3) {3:<46}|
    | 4) {4:<46}|
    | 5) {5:<46}|
    | 6) {6:<46}|
    | 7) {7:<46}|
    | 8) {8:<46}|
    | 9) {9:<46}|
    |==================================================|
    \"\"\".format("Title", "1", "2", "3", "4", "5", "6", "7", "8", "9"))""")


# Other
exercise_number = 1
desc = ""
border = "¬" * 69
menu_option = 0
toggle = 0
menu_status = "Off"

# Constants
MENU_EXIT = 5

# Inputs & processes
while menu_option != MENU_EXIT:
    main_menu_print()
    menu_option = int(input("Please enter and option from the menu: "))
    while menu_option < 1 or menu_option > MENU_EXIT:
        menu_option = int(input("Please enter a valid option from the menu: "))

    if menu_option == 1:
        exercise_number = input("Please enter the exercise number: ")
        if exercise_number != "":
            exercise_number = int(exercise_number)

    elif menu_option == 2:
        desc = input("Please enter a description of the exercise: ")

    elif menu_option == 3:
        if toggle == 0:
            menu_status = "On"
            toggle = 1
        else:
            menu_status = "Off"
            toggle = 0

    else:
        print(border)
        menu_head_print()
        exercise_head_print(exercise_number, desc)
        structure_print()
        print(border)
        input("Press enter to continue...")

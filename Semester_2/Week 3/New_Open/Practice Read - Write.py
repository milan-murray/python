"""
Milan Murray X00162027 | 12-Feb-2020 | Wednesday
Exercise 1:  Read/Write Menu System
"""
# Imports
from os import path
import time

# Other
main_menu = """\t|=======================================|
\t|{0:^39}|
\t|¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬|
\t| 1) {1:<35}|
\t| 2) {2:<35}|
\t| 3) {3:<35}|
\t| 4) {4:<35}|
\t|=======================================|\n""".format("Read & Write Menu", "Select File", "Read File", "Write File",
                                                        "Exit")
menu_option = 0
file_name = ""

# Constants
MENU_EXIT = 4

# Inputs & Processes
while menu_option != MENU_EXIT:
    if menu_option != 0:
        input("Press enter to continue...")
        print()
    print(main_menu)
    menu_option = int(input("Please select an option from the menu: "))

    while menu_option < 1 or menu_option > MENU_EXIT:
        menu_option = int(input("Please enter a valid option from the menu: "))

    if menu_option == 1:
        file_name = input("Please enter the name of the file: ")
        print("File name accepted.")

    elif menu_option == 2:
        if path.exists(file_name):
            content_of_file = open(file_name, "r")
            read_file = content_of_file.read()
            print(read_file)
            content_of_file.close()

        else:
            if file_name == "":
                print("There is no file selected.")
            else:
                print("Unknown file, please try again.")

    elif menu_option == 3:
        content_of_file = open(file_name, "w")
        content_of_file.write("¬¬¬¬¬¬¬¬¬¬¬¬" + time.strftime(" %d-%m-%Y, %H:%M ¬¬¬¬¬¬¬¬¬¬¬¬\n"))
        content_of_file.write(input("Please enter the text that you wish to write: "))
        content_of_file.write("\n¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬")
        content_of_file.close()

# Outputs

"""
Milan Murray X00162027 ¦ 22-Feb-2020 ¦ Saturday
Exercise 1: Create a system to store studied topics in text files and access them with a menu
"""
# Imports
from os import path


# Definitions
def main_menu_print(): print("""
    |==================================================|
    |{0:^50}|
    |--------------------------------------------------|
    | 1) {1:<46}|
    | 2) {2:<46}|
    | 3) {3:<46}|
    | 4) {4:<46}|
    | 5) {5:<46}|
    | 6) {6:<46}|
    |==================================================|
    """.format("OmniStudy", "Change document", "Access document", "Expand document", "Amend Document",
               "Create new document", "Exit"))


def file_print(file_name_in):
    with open(file_name_in) as read_file:
        content = read_file.read()
    print(content)


def file_create(file_name_in):
    with open(file_name_in, "w") as create_file:
        title = input("Please enter the title of the document: ")
        create_file.write(title + "\n¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬\n")
        create_lcv = 1
        while create_lcv == 1:
            stem = input("Please enter the keyword of the topic: ")
            branch = input("Please enter the explanation of the topic: ")
            create_file.write(stem + "\n")
            create_file.write("    > " + branch + "\n\n")
            create_lcv = int(input("Do you wish to add more \"1\", or return to main menu \"0\": "))


def file_expand(file_name_in):
    with open(file_name_in, "a") as append_file:
        create_lcv = 1
        while create_lcv == 1:
            stem = input("Please enter the keyword of the topic: ")
            branch = input("Please enter the explanation of the topic: ")
            append_file.write(stem + "\n")
            append_file.write("    > " + branch + "\n\n")
            create_lcv = int(input("Do you wish to add more \"1\", or return to main menu \"0\": "))


def file_amend(file_name_in):
    with open(file_name_in, "r") as amend_file:
        content = amend_file.read()
        old_text = input("Please enter the text to be replaced: ")
        if old_text in content:
            replace_text = input("Please enter the new text: ")
            content = content[:content.index(old_text)] + replace_text + content[content.index(old_text) +
                                                                                 len(old_text):]
        else:
            print("Could not find text.")

    with open(file_name_in, "w") as amend_file:
        amend_file.write(content)


# Other
menu_option = 0

# Constants
MENU_EXIT = 6
file_name = ""

# Inputs & processes
while menu_option != MENU_EXIT:
    if menu_option != 0:
        input("Press enter to continue...")
    main_menu_print()

    menu_option = int(input("Please select an option from the menu: "))
    print()
    while menu_option < 1 or menu_option > MENU_EXIT:
        menu_option = int(input("Please enter a valid option from the menu: "))
        print()

    if menu_option == 1:
        file_name = input("Please enter the name of the file: ")
        file_name += ".txt"
        if path.exists(file_name):
            print("File selected.")
        else:
            print(file_name, "does not exist.")
            file_name = ""

    elif menu_option == 2:  # Access
        if file_name != "":
            file_print(file_name)
        else:
            print("No file selected.")

    elif menu_option == 3:  # Expand
        if file_name != "":
            file_expand(file_name)
        else:
            print("No file selected.")

    elif menu_option == 4:  # Amend
        if file_name != "":
            file_amend(file_name)
        else:
            print("No file selected.")

    elif menu_option == 5:  # Create
        file_name = input("Please enter the name of the file to be created, or enter \"#\" to return to main menu: ")
        file_name += ".txt"
        while path.exists(file_name):
            file_name = input("File already exists. Enter a new name or enter \"#\" to return to main menu: ")
            file_name += ".txt"
        if file_name != "#.txt":
            file_create(file_name)
        else:
            file_name = ""

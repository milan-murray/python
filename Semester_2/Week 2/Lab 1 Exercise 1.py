"""
Milan Murray ¦ 06-Feb-2020 ¦ Thursday
Exercise 1:  Create a phone book system using a dictionary
"""
# Imports

# Other
phone_book_dict = {}
user_choice = 0

menu = """
\t|===============================|
\t|\t\t\tPhone Book\t\t\t|
\t|¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬|
\t|\t1) Look up a person\t\t\t|
\t|\t2) Add a person\t\t\t\t|
\t|\t3) Update a person\t\t\t|
\t|\t4) Delete a person\t\t\t|
\t|\t5) List of persons\t\t\t|
\t|\t6) Quit\t\t\t\t\t\t|
\t|===============================|
"""

# Constants
EXIT_VALUE = 6
PHONE_NUMBER_THRESHOLD_LOWER = 9
PHONE_NUMBER_THRESHOLD_HIGHER = 12

# Inputs & processes
while user_choice != EXIT_VALUE:
    print(menu)
    user_choice = int(input("Please select an option from the menu: "))
    while user_choice < 1 or user_choice > EXIT_VALUE:
        user_choice = int(input("Please select a valid numerical option from the menu: "))

    if user_choice == 1:
        print("\nLook up person:\n¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬")
        if phone_book_dict:
            search_name = input("Please enter the name of the person's telephone number you want to find: ")

            if search_name in phone_book_dict:
                print(search_name + ":", phone_book_dict[search_name])
            else:
                print("Nobody with the name", search_name, "is in the phone book.")

        else:
            print("Phone Book is empty.")

    elif user_choice == 2:
        print("\nAdd person:\n¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬")
        add_name = input("Please enter the name of the person to add to the phone book: ")

        if add_name not in phone_book_dict:
            phone_number = input("Please enter the phone number for this person: ")
            while len(phone_number) < PHONE_NUMBER_THRESHOLD_LOWER or len(phone_number) > PHONE_NUMBER_THRESHOLD_HIGHER:
                phone_number = input("Invalid phone number, please try again: ")
            phone_book_dict[add_name] = phone_number
            print("Person has been added.")

        else:
            print("This person already exists in the dictionary.")

    elif user_choice == 3:
        print("\nUpdate person:\n¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬")
        update_name = input("Please enter the name of the person you want to update: ")

        if update_name in phone_book_dict:
            phone_number = input("Please enter the new phone number for this person: ")
            while len(phone_number) < PHONE_NUMBER_THRESHOLD_LOWER or len(phone_number) > PHONE_NUMBER_THRESHOLD_HIGHER:
                phone_number = input("Please enter a valid phone number: ")

            if phone_number != phone_book_dict[update_name]:
                user_confirm = input("Are you sure you wish to change the number? Y/N: ")
                user_confirm = user_confirm.upper()

                if user_confirm == "Y":
                    phone_book_dict[update_name] = phone_number
                    print("Phone number updated.")
                else:
                    print("Phone number has not been changed.")

            else:
                print("The phone number is already up to date.")

        else:
            print("This person is not currently in the phone book.")

    elif user_choice == 4:
        del_name = input("Please enter the name of the person you want to remove form the phone book: ")
        if del_name in phone_book_dict:
            user_confirm = input("Are you sure you want to delete this user from the phone book? Y/N: ")
            user_confirm = user_confirm.upper()

            if user_confirm == "Y":
                del phone_book_dict[del_name]
                print("Person has been removed from the phone book.")
            else:
                print("Person was not removed from the phone book.")
        else:
            print("This person is not in the phone book.")

    elif user_choice == 5:
        print()
        if len(phone_book_dict) == 0:
            print("The phone book is currently empty.")
        else:
            print("Phone book:\n¬¬¬¬¬¬¬¬¬¬¬¬")
            for person in phone_book_dict:
                print(person + ":", phone_book_dict[person])

    if user_choice != 6:
        print()
        input("Press enter to continue..")

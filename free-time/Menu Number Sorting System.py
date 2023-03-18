"""
Milan Murray ¦ 16-Jan-2020 ¦ Thursday
Exercise: Create a menu system for generating and sorting a list.
"""
# Imports
import random
import time

# Other
user_choice = 0

# List elements
number_list = []
quantity_items_list = 0
upper_threshold = 0

lower_threshold = 0

main_menu = "\n\t¦=======================================¦\n" \
            "\t¦\t\t\t\tMain Menu\t\t\t\t¦\n" \
            "\t¦¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¦\n" \
            "\t¦\t1) View current list of numbers\t\t¦\n" \
            "\t¦\t2) Bubble sort the list\t\t\t\t¦\n" \
            "\t¦\t3) Generate new list\t\t\t\t¦\n" \
            "\t¦\t4) Exit\t\t\t\t\t\t\t\t¦\n" \
            "\t¦=======================================¦\n"


# Constants
MENU_START = 1
MENU_END = 4
ITEM_QUANTITY_LIMIT = 1000000000

# Processes
while user_choice != MENU_END:
    # Output main menu and input user's choice
    print(main_menu)
    user_choice = int(input("Please enter an option from the menu: "))
    print()

    while user_choice < MENU_START or user_choice > MENU_END:
        # Validation of user input
        user_choice = int(input("Please enter a valid option from the menu: "))

    if user_choice == 1:    # View current list
        # Validate list is not empty
        if number_list:
            print("The current list is:", number_list)
        else:
            print("The list is currently empty.")
        input("Press enter to continue...")

    elif user_choice == 2:  # Bubble sort
        sort_check = 1  # Prepare while LCV
        counter = 0     # Reset counter for amount of swaps
        # 50 numbers = <1 second
        # 175 numbers = c. 1 second
        # ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
        # RANGE: From -250 To 250 PRINTING: Every 5 swaps.
        # 250 numbers = c. 1 second ¦ 13940 swaps ¦ 16047 swaps ¦ 16056 swaps
        # 500 numbers = c. 8 seconds ¦ 60487 swaps ¦ 60451 swaps ¦ 62796 swaps
        # 750 numbers = c. 16.75 seconds ¦ 136850 swaps ¦ 140790 swaps ¦ 140958 swaps
        # 1000 numbers = c. 1 min, 3.8 seconds ¦ 237542 swaps ¦ 236370 swaps ¦ 246510 swaps
        # 1250 numbers = c. 1 min, 44 seconds ¦ 394,287 swaps
        # 1500 numbers = c. 2 mins, 3 seconds ¦ 554,749 swaps
        # 1750 numbers = c. 3 mins, 26 seconds ¦ 779,222 swaps
        # 2000 numbers = c. 6 mins, 5 seconds ¦ 975,385 swaps
        # 2500 numbers = c. 7 mins, 5 seconds ¦ 1,596,531 swaps
        # ¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬
        # RANGE: From -250 To 250 PRINTING: Every iteration
        # 5000 numbers = c. 6 hours

        # Validate list is not empty
        if number_list:
            start_time = time.strftime("%H Hours, %M Minutes, %S Seconds. Date: %d-%m-%y")
            start_time_seconds = (int(start_time[:2]) * (60 ** 2)) + (int(start_time[10:12]) * 60) + \
                                 (int(start_time[22:24]))
            print("Start time:", start_time)
            while sort_check != 0:  # LCV
                sort_check = 0
                for value in range(quantity_items_list - 1):
                    if number_list[value] > number_list[value + 1]:  # If the next number is smaller
                        counter += 1
                        print(number_list)
                        # If the list has been sorted this iteration it gets flagged to check again the next iteration
                        sort_check = 1
                        smaller_num = number_list[value + 1]  # Store the smaller number in another variable
                        # Replace the small number with the big number
                        number_list[value + 1] = number_list[value]
                        # Replace the big number with the small number
                        number_list[value] = smaller_num

            end_time = time.strftime("%H Hours, %M Minutes, %S Seconds. Date: %d-%m-%y")
            print("\nEnd time:", end_time)
            end_time_seconds = (int(end_time[:2]) * (60 ** 2)) + (int(end_time[10:12]) * 60) + \
                               (int(end_time[22:24]))

            elapsed_time_total_seconds = end_time_seconds - start_time_seconds
            """
            elapsed_time_hours = elapsed_time_total_seconds // (60 ** 2)
            elapsed_time_minutes = elapsed_time_total_seconds // 60
            elapsed_time_seconds = elapsed_time_total_seconds % (60 ** 2)
            """

            if start_time[40:] != end_time[40:]:
                elapsed_time_total_seconds = ()

            print("\nThe sorted number list is:", number_list)
            print("The size of the list:", quantity_items_list, "numbers.")
            print("It took", counter, "amount of number swaps to complete.")
            print("\nTime elapsed:", elapsed_time_total_seconds, "seconds.")
            input("Press enter to continue...")
        else:
            # If the list is empty
            print("The list is empty.")
            input("Press enter to continue...")

    elif user_choice == 3:  # Generate new list
        number_list = []     # Reset the list

        quantity_items_list = int(input("Please enter the desired amount of numbers in the list: "))
        # Prevent the user from creating a list too large
        while quantity_items_list < 1 or quantity_items_list > ITEM_QUANTITY_LIMIT:
            quantity_items_list = int(input("Quantity of items out of bounds! Please enter another number: "))

        # Input if the user wants to randomly generate numbers or use there own
        user_list_check = int(input("Enter \"0\" to randomly generate numbers, or enter \"1\" for your own numbers: "))
        while user_list_check != 0 and user_list_check != 1:    # Input validation
            user_list_check = int(input("Randomly generate numbers (0), or enter your own numbers? (1): "))

        if user_list_check == 0:    # Random generation
            lower_threshold = int(input("Please enter the lower threshold of the list: "))
            upper_threshold = int(input("Please enter the higher threshold of the list: "))
            for i in range(quantity_items_list):
                number_list.append(random.randint(lower_threshold, upper_threshold))
            print("New list generated:", number_list)
        else:
            for i in range(quantity_items_list):
                number_list.append(int(input("Enter a whole number to add to the list: ")))
            print("New list created:", number_list)
        input("Press enter to continue..")

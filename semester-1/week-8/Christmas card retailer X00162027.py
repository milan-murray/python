"""
Milan Murray 15/11/19
Python Lab 8:  Christmas card shop
"""
# Other
import time

# Initialise
total_daily_sales = 0
price_total = 0
option = 0
average_numbers_of_characters = 0
average_cost_of_cards_printed = 0
total_amount_of_characters = 0
return_counter = 0
total_refund_price = 0

main_menu = "\t\t▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲\n" \
            "\t\t⯈\t\tChristmas Card Shop\t\t\t⯇\n" \
            "\t\t▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼\n" \
            "\t\t⯈ 1) Sale\t\t\t\t\t\t\t⯇\n" \
            "\t\t⯈ 2) Return\t\t\t\t\t\t⯇\n" \
            "\t\t⯈ 3) Run Report\t\t\t\t\t⯇\n" \
            "\t\t⯈ 4) Exit\t\t\t\t\t\t\t⯇\n" \
            "\t\t▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼\n"

sale_menu = "\t\t▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲\n" \
            "\t\t⯈\tChristmas Card Creator - Sale\t⯇\n" \
            "\t\t▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼\n"

return_menu = "\t\t▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲\n" \
              "\t\t⯈\tChristmas Card Creator - Return\t⯇\n" \
              "\t\t▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼\n"

report_menu = "\t\t▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲\n" \
              "\t\t⯈\tChristmas Card Creator - Report\t⯇\n" \
              "\t\t▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼\n"

end_program = "\t\t▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲\n" \
              "\t\t⯈\tThank you for using the Christmas Card Shop\t⯇\n" \
              "\t\t▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼▲▼"

# Constants
PRICE_CARD = 4.0  # Card base price
MAX_CARD_LEN = 100  # Used to prevent cards from being over 100 characters in length

# Inputs (Output main menu)
print()
print(main_menu)

# Processes
while option != 4:
    option = int(input("Please choose a option: "))
    print()

    while option < 1 or option > 4:     # Input validation for option
        option = int(input("Please enter a valid option: "))
        print()

    if option == 1:     # Sale menu
        price_characters = 0    # Initialise characters
        print()
        print(sale_menu)

        personal_message = input("Please enter your personal message: ")
        while len(personal_message) >= MAX_CARD_LEN:     # Input validation for personal message
            personal_message = input("Too many characters. Please enter your personal message: ")

        price_characters += (0.5 * len(personal_message))       # Cost of characters
        price_total_current = PRICE_CARD + price_characters     # Total price calculation for card

        print("Number of characters printed:", len(personal_message))
        total_amount_of_characters += len(personal_message)     # Used for average characters
        print("Cost of characters printed:", price_characters, "euro.")
        print("Sale total:", price_total_current, "euro.")
        print(time.strftime("Sale complete: %d/%m/%y at %H:%M"))
        total_daily_sales += 1  # Total sales counter
        price_total += price_total_current      # Update the final price for report
        input("Press enter to return to the main menu...")  # Optional buffer to prevent scrolling past
        print()
        print(main_menu)

    elif option == 2:
        print(return_menu)
        refund = float(input("Please enter the price of the card to be returned: "))
        total_refund_price += refund
        return_counter += 1
        print()
        print(main_menu)

    elif option == 3:   # Report menu
        if total_daily_sales > 0:
            average_numbers_of_characters = total_amount_of_characters / total_daily_sales
            average_numbers_of_characters = round(average_numbers_of_characters, 2)
            average_cost_of_cards_printed = price_total / total_daily_sales
            average_cost_of_cards_printed = round(average_cost_of_cards_printed, 2)
        else:
            average_numbers_of_characters = 0

        print(report_menu)
        print("Total sales: €", price_total)
        print("Number of sales:", total_daily_sales)
        print("Average number of characters printed:", average_numbers_of_characters)
        print("Average cost of a card:", average_cost_of_cards_printed)
        print("Number of returns:", return_counter)
        if return_counter > 0:
            print("Cost of returns: €", total_refund_price)
        input("Press enter to return to the main menu...")  # Optional buffer to prevent scrolling past
        print()
        print(main_menu)

print(end_program)

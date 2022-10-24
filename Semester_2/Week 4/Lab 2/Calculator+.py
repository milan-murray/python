"""
Milan Murray X00162027 Ayesha Cortado X00165424 ¦ 21-Feb-2020 ¦ Friday
Exercise: Create a calculator system with additional functionality
"""
# Imports


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
    | 7) {7:<46}|
    | 8) {8:<46}|
    | 9) {9:<46}|
    |==================================================|
    """.format("Calculator+", "Add", "Subtract", "Multiply", "Divide", "Raise to the power", "List of squares",
               "Encrypt a message", "Upper and lower case", "Exit"))


def add_print_nums(add_num1_in, add_num2_in):
    add_ans = add_num1_in + add_num2_in
    print(add_num1_in, "+", add_num2_in, "=", add_ans)


def sub_print_nums(sub_num1_in, sub_num2_in):
    sub_ans = sub_num1_in - sub_num2_in
    print(sub_num1_in, "-", sub_num2_in, "=", sub_ans)


def mul_print_nums(mul_num1_in, mul_num2_in):
    mul_ans = mul_num1_in * mul_num2_in
    print(mul_num1_in, "*", mul_num2_in, "=", mul_ans)


def div_print_nums(div_num1_in, div_num2_in):
    div_ans = div_num1_in / div_num2_in
    print(div_num1_in, "/", div_num2_in, "=", div_ans)


def power_print_nums(power_num1_in, power_num2_in):
    power_ans = power_num1_in ** power_num2_in
    print(power_num1_in, "to the power of", power_num2_in, "=", power_ans)


def l_square_print(range_threshold_lower_in, range_threshold_upper_in):
    print("The value's in this range squared are: ", end="")
    for value in range(range_threshold_lower_in, range_threshold_upper_in + 1):
        l_s_ans = value ** 2
        print(l_s_ans, end=" ")
    print()


def message_encrypt_print(message_in, key_in):
    encrypted_ms = ""

    for char in message_in:
        char_value = ord(char)
        encrypt_value = char_value + key_in
        if encrypt_value > ord("z"):
            encrypt_value -= MAX_KEY
        encrypted_ms += chr(encrypt_value)
    print(message_in, "has been encrypted to: ", encrypted_ms)


def count_lower_upper_chars(user_sentence_in):
    lower_char_counter = 0
    upper_char_counter = 0
    for char in user_sentence_in:
        if char.isupper():
            upper_char_counter += 1
        elif char.islower():
            lower_char_counter += 1
    print("Amount of upper case characters: ", upper_char_counter)
    print("Amount of lower case characters: ", lower_char_counter)


# Other
menu_option = 0

# Constants
MENU_EXIT = 9
MAX_KEY = 26

# Inputs & processes
while menu_option != MENU_EXIT:
    if menu_option != 0:
        input("Press enter to continue...")
    main_menu_print()
    menu_option = int(input("Please enter an option from the menu: "))
    while menu_option < 1 or menu_option > MENU_EXIT:
        menu_option = int(input("Please enter a valid option from the menu: "))

    if menu_option == 1:
        add_num1 = float(input("Please enter the first number to be added: "))
        add_num2 = float(input("Please enter the second number to be added: "))
        add_print_nums(add_num1, add_num2)

    elif menu_option == 2:
        sub_num1 = float(input("Please enter the first number to be subtracted: "))
        sub_num2 = float(input("Please enter the second number to be subtracted: "))
        sub_print_nums(sub_num1, sub_num2)

    elif menu_option == 3:
        mul_num1 = float(input("Please enter the first number to be multiplied: "))
        mul_num2 = float(input("Please enter the second number to be multiplied: "))
        mul_print_nums(mul_num1, mul_num2)

    elif menu_option == 4:
        div_num1 = float(input("Please enter the first number to be divided: "))
        div_num2 = float(input("Please enter the second value to be the denominator (non 0): "))
        while div_num2 == 0:
            div_num2 = float(input("Please enter a non zero value for the denominator: "))
        div_print_nums(div_num1, div_num2)

    elif menu_option == 5:
        power_num1 = float(input("Please enter the first number to be raise by a power: "))
        power_num2 = float(input("Please enter the second number to be the power (0 or greater): "))
        while power_num2 < 0:
            power_num2 = float(input("Please enter a valid number (0 or greater): "))
        power_print_nums(power_num1, power_num2)

    elif menu_option == 6:
        range_threshold_lower = int(input("Please enter the lower value threshold: "))
        range_threshold_upper = int(input("Please enter the upper value threshold: "))
        while range_threshold_lower >= range_threshold_upper:
            range_threshold_upper = int(input("Please enter a value greater than the lower threshold: "))
        l_square_print(range_threshold_lower, range_threshold_upper)

    elif menu_option == 7:
        message = input("Please enter a message to be encrypted (no spaces or lowercase): ")
        message = message.lower()
        while " " in message:
            message = input("Please enter a message with no spaces: ")
        key = int(input("Please enter a key (Between 1 and 25 inclusive): "))
        while key < 1 or key > MAX_KEY - 1:
            key = int(input("Please enter a key (Between 1 and 25 inclusive): "))
        message_encrypt_print(message, key)

    elif menu_option == 8:
        user_sentence = input("Please enter a sentence: ")
        count_lower_upper_chars(user_sentence)

print("Calculator+ closed.")

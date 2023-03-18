"""
Milan Murray 08/11/2019
Exercise 1: Add the numbers between 50 and 100 (inclusive) using while and for loops.
"""
print("\n---\tExercise 1: Add the numbers between 50 and 100 (inclusive) using while and for loops.\t---\n")
# Other
counter_while = 50
total_sum_while = 0
total_sum_for = 0

# Constants
THRESHOLD_HIGHER = 101
THRESHOLD_LOWER = 50

# Inputs

# Processes
while counter_while < THRESHOLD_HIGHER:
    total_sum_while += counter_while
    counter_while += 1

for counter_for in range(THRESHOLD_LOWER, THRESHOLD_HIGHER):
    total_sum_for += counter_for

# Outputs
print("The sum of numbers from 50 to 100 (inclusive) using a while loop:", total_sum_while)
print("The sum of numbers from 50 to 100 (inclusive) using a for loop:", total_sum_for)


"""
Milan Murray 08/11/2019
Exercise 2: Allow the user to input 5 floating point numbers using a for loop, print the average.
"""
print("\n---\tExercise 2: Allow the user to input 5 floating point numbers using a for loop, print the average.\t---\n")
# Other
sum_numbers = 0

# Constants
AMOUNT_OF_NUMBERS = 5
SIGNIFICANT_FIGURES = 2

# Inputs

# Processes
for counter in range(0, AMOUNT_OF_NUMBERS):
    number = float(input("Please enter a number: "))
    sum_numbers += number

average_of_numbers = sum_numbers / AMOUNT_OF_NUMBERS
average_of_numbers = round(average_of_numbers, SIGNIFICANT_FIGURES)

# Outputs
print("The average of these numbers are:", average_of_numbers)


"""
Milan Murray 08/11/2019
Exercise 3: Add all the even and odd numbers between 1 and 20 separately. Print the results of both.
"""
print("\n---\tExercise 3: Add all the even and odd numbers between 1 and 20 separately. "
      "Print the results of both.\t---\n")
# Other
counter = 0
even_sum = 0
odd_sum = 0

# Constants

# Inputs

# Processes
for counter in range(1, 21):
    if counter % 2 == 0:
        even_sum += counter
    else:
        odd_sum += counter

# Outputs
print("The sum of the even numbers between 1 and 20 are:", even_sum)
print("The sum of the odd numbers between 1 and 20 are:", odd_sum)


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


"""
Milan Murray 08/11/2019
Exercise 5: Calculate the number of commas in a string to be inputted by the user.
"""
print("\n---\tExercise 5: Calculate the number of commas in a string to be inputted by the user.\t---\n")
# Other
current_comma_location = 0
comma_counter = 0

# Constants

# Inputs
users_word = input("Please enter a sentence with commas: ")
length_of_string = len(users_word)
remainder_of_word = users_word[0:]

# Processes
while "," in remainder_of_word:
    # print(remainder_of_word)  # Useful to visualise the logic.
    comma_counter += 1
    current_comma_location = remainder_of_word.index(",")
    remainder_of_word = remainder_of_word[(current_comma_location + 1):]

# Outputs
if length_of_string == 1:
    print("Your sentence has", length_of_string, "character.")
else:
    print("Your sentence has", length_of_string, "characters.")
if comma_counter == 1:
    print("There is", comma_counter, "comma in the entered text.")
else:
    print("There are", comma_counter, "commas in the entered text.")


"""
Milan Murray 08/11/2019
Exercise 6: Input a starting number, ending number & step for a counting program. Output each number and the sum.
"""
print("\n---\tExercise 6: Input a starting number, ending number & step for a counting program.\t---\n")
# Other
sum_of_counter = 0

# Constants

# Inputs
start_number = int(input("Please enter the starting number: "))
ending_number = int(input("Please enter the ending number (inclusive): "))
step = int(input("Please enter the step the counter should take: "))

# Processes
ending_number += 1

for counter in range(start_number, ending_number, step):
    print(counter)
    sum_of_counter += counter
    print("Sum of counter:", sum_of_counter)

# Outputs
print("The sum of these numbers is:", sum_of_counter)


"""
Milan Murray 08/11/2019
Exercise 7: Determine if an inputted year is a leap year or not.
"""
print("\n---\tExercise 7: Determine if an inputted year is a leap year or not.\t---\n")
# Other

# Constants
LEAP_DIVISOR_RULE_1 = 4
LEAP_DIVISOR_RULE_2 = 100
LEAP_DIVISOR_RULE_3 = 400

# Inputs
year = int(input("Please enter a year: "))

# Processes
if year % LEAP_DIVISOR_RULE_1 == 0:
    if year % LEAP_DIVISOR_RULE_2 != 0:
        leap_year = True    # If divisible by 4 & not divisible by 100: True
    else:
        if year % LEAP_DIVISOR_RULE_3 == 0:
            leap_year = True    # If divisible by 4 & divisible by 100 & divisible by 400: True
        else:
            leap_year = False   # If divisible by 4 & not divisible by 100 & divisible by 400: False
else:
    leap_year = False   # If not divisible by 4: False

# Outputs
print("The year you have entered is:", year)
print("Leap year:", leap_year)

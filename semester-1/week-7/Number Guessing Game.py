"""
Milan Murray 07/11/2019
Number Guessing Game
"""
# Other
import random
the_number = random.randint(1, 1000)
attempts = 1
# Constants


# Inputs
guess_number = int(input("Guess a number from 1 to 1000: "))

# Processes
while guess_number != the_number and attempts < 20:
    attempts += 1
    if guess_number > the_number:
        print("Your guess is too high. Try again")
        guess_number = int(input("Please enter another number: "))
    elif guess_number < the_number:
        print("Your guess is too low. Try again")
        guess_number = int(input("Please enter another number: "))
else:
    if attempts > 3:
        print("Too many guesses")
        print("The number was:", the_number)
    else:
        print("Game over. GG.")
        print("The number was:", the_number)

# Outputs
if attempts == 1:
    print("It took you", attempts, "attempt to find the number.")
else:
    print("It took you", attempts, "attempts to find the number.")

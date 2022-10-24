"""
Milan Murray X00162027 & Soulman Dembele X00168352| 14-Feb-2020 | Friday
Exercise 1:  Create a trivia quiz using a text file.
"""
# Imports

# Other
user_score = 0

# Constants
AMOUNT_OF_TOTAL_QUESTIONS = 3
QUESTION_OPTIONS = 4

# Inputs & Processes
with open("quiz.txt", "r") as text_file:
    title = text_file.readline()
    print(title + "There will be 4 options for each question, try get the correct answer!\n", end="")

    for index in range(AMOUNT_OF_TOTAL_QUESTIONS):   # Per Question
        category = text_file.readline()
        print(category, end="")
        question = text_file.readline()
        print(question, end="")

        question_list = []
        for i in range(QUESTION_OPTIONS):   # Per question option
            question_list.append(text_file.readline())
            print(str(i + 1) + ":", question_list[i], end="")

        ans = int(text_file.readline())
        user_choice = int(input("Pick an answer from the list: "))
        while user_choice < 0 or user_choice > QUESTION_OPTIONS:
            user_choice = int(input("Please enter a valid option: "))
        if user_choice == ans:
            print("Correct!")
            user_score += 1
        else:
            print("Wrong!")
        print(text_file.readline())
        print("Score:", user_score)
        input("Press enter to continue...")

# Outputs
print("That's it!", "\nYour final score is:", user_score)

"""
Milan Murray 29/11/19
Exercise 1: Electoral Voting System
"""
# Other
candidate_list = []
vote_results_list = []
total_votes = 0
average_votes = 0
lowest_votes = 0

# Constants
PERCENT_MULTIPLE = 100
AMOUNT_OF_CANDIDATES = 5

# Processes
for candidate in range(AMOUNT_OF_CANDIDATES):
    candidate_list.append(input("Please enter the last name of a candidate: "))
    vote = int(input("Please enter the amount of votes received by this candidate: "))
    vote_results_list.append(vote)
    total_votes += vote

average_votes = total_votes / AMOUNT_OF_CANDIDATES
winner = candidate_list[vote_results_list.index(max(vote_results_list))]
lowest_votes = candidate_list[vote_results_list.index(min(vote_results_list))]
# Outputs
print()
print("Candidate\t\t\tVotes Received\t\t\tPercent of total votes")

for index, candidate in enumerate(candidate_list):
    percent_total_votes = ((vote_results_list[index] / total_votes) * PERCENT_MULTIPLE)
    percent_total_votes = round(percent_total_votes, 2)
    print("{0:10}\t\t\t{1:<10}\t\t\t\t{2:<4}".format(candidate, vote_results_list[index], percent_total_votes))

print()
print("Total votes:", total_votes)
print("Average:", average_votes)
print()
print("Winner:", winner)
print("Lowest Votes:", lowest_votes)


"""
Milan Murray 29/11/19
Exercise 2: Track hours worked of college department
"""
# Other
total_hours_worked = 0
hours_per_day_list = []
days_list = ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5"]
days_over_six_hours = 0

# Constants
WORKING_DAYS = 5
MIN_WORKING_HOURS = 0
MAX_WORKING_HOURS = 9
OVER_SIX_HOURS = 6
SIGNIFICANT_FIGURE = 2

# Processes
for value in range(WORKING_DAYS):
    hours = int(input("Please enter the amount of hours worked: "))
    while hours < MIN_WORKING_HOURS or hours > MAX_WORKING_HOURS:
        hours = int(input("Please enter a valid amount of hours: "))
    if hours > OVER_SIX_HOURS:
        days_over_six_hours += 1
    hours_per_day_list.append(hours)
    total_hours_worked += hours

average_hours_worked = total_hours_worked / WORKING_DAYS
average_hours_worked = round(average_hours_worked, SIGNIFICANT_FIGURE)

# Outputs
print("\nHours worked per day:")
for index in range(WORKING_DAYS):
    print(days_list[index] + ":", hours_per_day_list[index])
print("\nAverage hours worked:", average_hours_worked)
print("Total hours worked:", total_hours_worked)
print("Amount of days worked over 6 hours:", days_over_six_hours)

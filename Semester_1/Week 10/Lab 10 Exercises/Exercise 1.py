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
AMOUNT_OF_CANDIDATES = 4

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

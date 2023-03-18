"""
Milan Murray 06/12/19
Exercise 1: Candidate Voting Program
"""
# Other
candidates = []
winners = []
losers = []
total_votes = 0

table1 = "¦ Name\t\t\t\tVotes\t\t\t\tConstituency\t\tVote Percentage ¦\n" \
         "¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬"

table2 = "¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬\n"

# Constants
AMOUNT_CANDIDATES = 3
PERCENT_SIGNIFICANT_FIGURE = 2

# Inputs
for index in range(AMOUNT_CANDIDATES):
    print("Please enter the last name of the candidate", index + 1, end="")
    c_name = input(": ")
    votes = int(input("Please enter the amount of votes awarded to this candidate: "))
    total_votes += votes
    constituency = input("Please enter the candidate's constituency: ")
    candidates.append([c_name, votes, constituency])
    print()

# Processes
vote_list = [index[1] for index in candidates]

# Before optional part
"""
winner = candidates[vote_list.index(max(vote_list))][0]
least_pop_candidate = candidates[vote_list.index(min(vote_list))][0]
"""

# Optional Part
for index, amount_votes in enumerate(vote_list):
    if amount_votes == max(vote_list):
        winners.append(candidates[index][0])
    if amount_votes == min(vote_list):
        losers.append(candidates[index][0])

# Percentage calculation
for candidate in candidates:
    percentage_of_votes = (candidate[1] / total_votes) * 100
    percentage_of_votes = round(percentage_of_votes, PERCENT_SIGNIFICANT_FIGURE)
    candidate.append(percentage_of_votes)

# Outputs
print(table1)
for candidate in candidates:
    for item in candidate:
        print("{0:<20}".format(item), end="")
    print()
print(table2)

print("Winners: ", end="")
for candidate in winners:
    print(candidate, end="\t\t")
print()
print("The least popular candidates: ", end="")
for candidate in losers:
    print(candidate, end="\t\t")

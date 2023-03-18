"""
Milan Murray 15/12/19
NEW: Dictionary!
"""
# Other
jugedores_dict = {1: "Milan", 2: "Jonas", 3: "Jarell"}

# Constants

# Input
player = int(input("Please enter the number of the player: "))

# Processes
if player in jugedores_dict:
    player_name = jugedores_dict[player]
    print("\nThis player, number", str(player) + ", is", player_name + ".")
else:
    print("\nThis player, number", str(player) + ", does not exist.")

# Input
player = int(input("What position do you want to insert a player into?: "))

# Processes
if player in jugedores_dict:
    print("Warning, this will replace a player in the dictionary!")
player_name = input("Please enter the name of the player: ")
jugedores_dict[player] = player_name

# Input
player = int(input("Please enter the position of the player you wish to delete: "))

# Processes
if player in jugedores_dict:
    del jugedores_dict[player]
    print("ERADICATED")
else:
    print("Impossible")

# Outputs
print(jugedores_dict)
"""
if 2 in jugedores_dict:
    print(jugedores_dict[2])
else:
    print("Dictionary key 2 does not exist.")

if 4 in jugedores_dict:
    print(jugedores_dict[4])
else:
    print("Dictionary key 4 does not exist.")
"""

print(jugedores_dict.get(2, "Dictionary key 2 does not exist."))
print(jugedores_dict.get(4, "Dictionary key 4 does not exist."))

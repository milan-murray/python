"""
Milan Murray 27/09/2019
Week 2 Lab
"""

NUMBER_OF_COINS = float(107)
NUMBER_OF_PIRATES = float(4)

share_of_coins = NUMBER_OF_COINS//NUMBER_OF_PIRATES

remainder = NUMBER_OF_COINS%NUMBER_OF_PIRATES

print("Each pirate will get", int(share_of_coins), "gold coins each.")
print("There will be ", int(remainder), "gold coins left over.")

"""
Tosin & Milan 24/10/19
PBL Week 6
"""

# Constants
TOFU_BURGER = 3.49
CAJUN_CHICKEN = 4.59
BUFFALO_WINGS = 3.99
RAINBOW_FILLET = 2.99

RICE_CRACKER = 0.79
NO_SALT_CHIPS = 0.69
ZUCCHINI = 1.09
BROWN_RICE = 0.59

CAFE_MOCHA = 1.99
CAFE_LATTE = 1.99
ESPRESSO = 2.49
OOLONG_TEA = 0.99

# Input
selection_entree = int(input("Please enter the number of your entree: "))
quantity_entree = int(input("Please enter the quantity of your entree: "))
selection_side = int(input("Please enter the number of your side: "))
quantity_side = int(input("Please enter the quantity of your side: "))
selection_drink = int(input("Please enter the number of your drink: "))
quantity_drink = int(input("Please enter the quantity of your drinks: "))
menu1 = "1"
menu2 = "2"
menu3 = "3"
# Outputs
print(menu1, menu2, menu3)

# Processes
if selection_entree == 1:
    selection_entree = "Tofu Burger"
    price_entree = TOFU_BURGER
elif selection_entree == 2:
    selection_entree = "Cajun Chicken"
    price_entree = CAJUN_CHICKEN
elif selection_entree == 3:
    selection_entree = "Buffalo Wings"
    price_entree = BUFFALO_WINGS
elif selection_entree == 4:
    selection_entree = "Rainbow Fillet"
    price_entree = RAINBOW_FILLET
else:
    selection_entree = "Unknown"
    price_entree = 0

price_entree *= quantity_entree
price_entree = str(price_entree)

if selection_side == 1:
    selection_side = "Rice Cracker"
    price_side = RICE_CRACKER
elif selection_side == 2:
    selection_side = "No Salt Chips"
    price_side = NO_SALT_CHIPS
elif selection_side == 3:
    selection_side = "Zucchini"
    price_side = ZUCCHINI
elif selection_side == 4:
    selection_side = "Brown Rice"
    price_side = BROWN_RICE
else:
    selection_side = "Unknown"
    price_side = 0

price_side *= quantity_side
price_side = str(price_side)

if selection_drink == 1:
    selection_drink = "Café Mocha"
    price_drink = CAFE_MOCHA
elif selection_drink == 2:
    selection_drink = "Café Latte"
    price_drink = CAFE_LATTE
elif selection_drink == 3:
    selection_drink = "Espresso"
    price_drink = ESPRESSO
elif selection_drink == 4:
    selection_drink = "Oolong Tea"
    price_drink = OOLONG_TEA
else:
    selection_drink = "Unknown"
    price_drink = 0

price_drink *= quantity_drink
price_drink = str(price_drink)

# Output
print("Your order: ")
print("Entree: ", quantity_entree, selection_entree, "€" + price_entree)
print("Side dish: ", quantity_side, selection_side, "€" + price_side)
print("Drink: ", quantity_drink, selection_drink, "€" + price_drink)
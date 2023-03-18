"""
Milan Murray 17/11/19
Additional Questions
"""

"""
# Other
import math

cycle = 0   # Used to maintain loop

main_menu = "\t\t¦===============================================¦\n" \
            "\t\t¦\tCalculation of volume for a solid object\t¦\n" \
            "\t\t¦¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¦\n" \
            "\t\t¦\t1. Cube\t\t\t\t\t\t\t\t\t\t¦\n" \
            "\t\t¦\t2. Cylinder\t\t\t\t\t\t\t\t\t¦\n" \
            "\t\t¦\t3. Sphere\t\t\t\t\t\t\t\t\t¦\n" \
            "\t\t¦\t4. Exit\t\t\t\t\t\t\t\t\t\t¦\n" \
            "\t\t¦===============================================¦\n"

# Constants
VOLUME_POWER = 3
SPHERE_MATH_ELEMENT = 4 / 3

# Inputs
print("\n---\t\tQuestion 1: A program that calculates the volumes of different solids.\t\t---\n")
print(main_menu)
option = int(input("Please chose an option from the menu: "))
print()

# Processes
while option != 4:
    cycle += 1
    if cycle > 1:
        print(main_menu)
        option = int(input("Please chose an option from the menu: "))
        print()
    while option < 0 or option > 4:
        option = int(input("Please re-enter a valid option: "))
        print()

    if option == 1:     # Cube: v = length ** 3
        side_length = float(input("Please enter the side length of the cube: "))
        cube_volume = side_length ** VOLUME_POWER
        cube_volume = round(cube_volume, 2)
        print("The volume of a cube of side length", side_length, "units is:", cube_volume, "units squared.")
        input("Press enter to continue...")
        print()

    elif option == 2:   # Cylinder: v = p * r2 * height
        radius = float(input("Please enter the radius of the cylinder: "))
        height = float(input("Please enter the height of the cylinder: "))
        cylinder_volume = math.pi * (radius ** 2) * height
        cylinder_volume = round(cylinder_volume, 2)
        print("The volume of a cylinder with radius", radius,
              "and height", height, "is", cylinder_volume, "units squared")
        input("Press enter to continue...")
        print()

    elif option == 3:   # Sphere: v = (4 / 3) * p * r3
        radius = float(input("Please enter the radius of the sphere:"))
        sphere_volume = SPHERE_MATH_ELEMENT * math.pi * (radius ** VOLUME_POWER)
        sphere_volume = round(sphere_volume, 2)
        print("The volume of a sphere of radius", radius, "is:", sphere_volume, "units squared.")
        input("Press enter to continue...")
        print()

print("Task failed successfully")
"""

# """
# Other

# Constants

# Inputs
print("\n---\tExercise 2: Format a URL\t---\n")
sentence = input("Please enter the desired URL for the website: ")
remainder_sentence = sentence

# Processes
while " " in remainder_sentence:
    space_loc = (remainder_sentence.index(" ") + 1)     # Find where the space is in the remainder of the sentence
    # remainder_sentence = remainder_sentence[space_loc:]     # Setup the remainder of the sentence for the next loop
    start_sentence = remainder_sentence[:sentence.index(" ")]   # Prepare the new sentence for adding 20%
    new_start = start_sentence + "%20"  # add 20% to the end of the string
    remainder_sentence = new_start + remainder_sentence     # The final is the original gaining a 20% each loop

    print(new_start)
    print(remainder_sentence)

# Outputs

# """

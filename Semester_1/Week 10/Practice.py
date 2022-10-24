"""
Milan Murray 28/11/19
NEW:    Enumeration!
        Format!
        List Sorting!

"""
# Other
my_list = [1, 19, 27, 8, 5, 9]

# Constants


# Inputs


# Processes
# Enumerate basics
print(my_list)
for index, item in enumerate(my_list):
    if item > 10:
        my_list[index] = 10
print(my_list)
print()
print("Index\t\tItem")
for index, item in enumerate(my_list):
    print(index, "\t\t\t", item)
input("Press enter to continue...")

# Format
print("XxX420Sammy69Boi360XxX has {0:<1} red {1:16}".format(555555, "balloons"))

# COMBINATION
for index, item in enumerate(my_list):
    print("{0:1}\t\t\t{1:2}".format(index, item))

# Sort
sorted_list = sorted(my_list)
print()
# Outputs



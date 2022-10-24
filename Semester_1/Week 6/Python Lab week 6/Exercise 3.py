"""
Milan Murray 25/10/19
Exercise 3: Develop a program that inputs the users full name, separated by a space. Output name and initials.
"""
# Constants

# Inputs
full_name = input("Please enter your full name separated by a space: ")

# Processes
space_loc = full_name.index(" ")

f_name = full_name[0:space_loc]
s_name = full_name[(space_loc + 1):]

f_name = f_name.capitalize()
s_name = s_name.capitalize()

initial_f = f_name[0]
initial_s = s_name[0]
full_name = full_name.capitalize()

# Outputs
print("Your full name is:", f_name, s_name)

"""
print("Your full name is: ", full_name)
print("Your initials are:", initial_f + initial_s)
"""

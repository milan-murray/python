"""
Milan Murray 04/10/19
Visualise the diameter of a circle.
"""
# Constants

# Inputs
radius = int(input("Please enter a radius: ",))

# Processing
radius_visual = "-" * radius
diameter_visual = "-" * (radius * 2)

# Outputs
print("The radius is this long: ", radius_visual)
print("The diameter would be this long: ", diameter_visual)
"""
Milan Murray 04/10/19
Exercise 1: Converting hours, minutes and seconds into seconds.
"""

# Constants
SECONDS_PER_MINUTE = 60
MINUTES_PER_HOUR =  60

# Inputs
hours = int(input("Hours: "))
minutes = int(input("Minutes: "))
seconds = int(input("Seconds: "))

# Processing
combined_minutes = (hours * MINUTES_PER_HOUR) + minutes
combined_seconds = (combined_minutes * SECONDS_PER_MINUTE) + seconds

# Outputs
print("This time in hours, minutes and seconds is equivalent to ", combined_seconds,"seconds.")
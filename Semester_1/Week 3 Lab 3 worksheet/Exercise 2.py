"""
Milan Murray 04/10/19
Exercise 2: Convert seconds into hours, minutes and seconds.
"""

# Constants
SECONDS_PER_MINUTE = 60
MINUTES_PER_HOUR = 60
SECONDS_PER_HOUR = 60 ** 2

# Inputs
total_seconds = int(input("Enter time in seconds: "))

# Processing
hours = total_seconds // SECONDS_PER_HOUR
minutes = total_seconds % SECONDS_PER_HOUR
combined_minutes = minutes // MINUTES_PER_HOUR
seconds = minutes % SECONDS_PER_MINUTE

# Outputs
print("Hours: ", hours)
print("Minutes: ", combined_minutes)
print("Seconds: ", seconds)

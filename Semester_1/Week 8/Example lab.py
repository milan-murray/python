lower_n = int(input("Please enter the lower number: "))
higher_n = int(input("Please enter the higher number: "))
value = int(input("Please enter a number: "))

while value < lower_n or value > higher_n:
    value = int(input("Please enter another value: "))
print("This value", value, "is within the range.")

number = int(input("Please enter a number: "))

ans = 1

if number < 0:
    print("Error.")
else:
    for i in range(number, 0, -1):
        ans *= i

print(ans, "\n")

ans = 1

for i in range(1, number + 1):
    ans *= i

print(ans)

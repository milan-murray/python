number = int(input("Please enter a number: "))
power = int(input("Please enter a power: "))

if power >= 0:
    if power == 0:
        if number == 0:
            ans = 0
            print(ans)
        else:
            ans = 1     # Power = 0, number > 0.
            print(ans)
    else:
        ans = number ** power
        print(ans)
else:
    print("Error")

b = int(input("Enter number: "))
for x in range(1, b+1):
    if x % 20 == 0:
        print("Twist")
    elif x % 15 == 0:
        pass
    elif x % 5 == 0:
        print("Fizz")
    elif x % 3 == 0:
        print("Buzz")
    else:
        print(x)
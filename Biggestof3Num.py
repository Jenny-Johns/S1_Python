# biggest of 3 number
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
z = int(input("Enter the third number: "))

if x > y:
    if x > z:
        print("{} is the biggest".format(x))
    else:
        print("{} is the biggest".format(z))
elif y > z:
    print("{} is the biggest".format(y))
else:
    print("{} is the biggest".format(z))

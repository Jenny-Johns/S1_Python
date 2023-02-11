# Leap year #
cr = int(input("Enter the current year:"))
fi = int(input("Enter the final year:"))
print("The next leap years:")
while cr <= fi:
    if cr % 4 == 0:
        print(cr)
        cr = cr+1
    else:
        cr = cr+1

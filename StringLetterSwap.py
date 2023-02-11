# exchanging first char of two string #
a = input("Enter the first string:")
a1 = a[0]
b = input("Enter the second string:")
b1 = b[0]
ab = b1[0]+a[1:]
ba = a1[0]+b[1:]
print(ab + " " + ba)

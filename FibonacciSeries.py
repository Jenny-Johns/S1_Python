# fibonacci series #
li = int(input("Enter the limit: "))
a = 0
b = 1
c = 0
i = 0
while i <= li:
    print(a)
    c = a+b
    a = b
    b = c
    i = i+1


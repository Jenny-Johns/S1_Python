# factorial of a number
a = int(input("Enter the number to find factorial :"))
i = 1
f = 1
while i <= a:
    f = f*i
    i = i+1
print("factorial of {} is".format(a), f)

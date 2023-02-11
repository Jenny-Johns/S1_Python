# Factors of a number #
n = int(input("Enter the number: "))
print("factors of {}:".format(n))
for i in range(1, n+1, 1):
    if n % i == 0:
        print(i)
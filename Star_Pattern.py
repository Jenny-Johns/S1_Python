# * pattern #
limit = int(input("Enter the limit: "))
i = 0
while i <= limit:
    j = 0
    while j < i:
        print("*", end=" ")
        j = j+1
    i = i+1
    print("\n")
i = 0
while i <= limit:
    j = limit
    while j >= i:
        print("*", end=" ")
        j = j-1
    print("\n")
    i = i+1

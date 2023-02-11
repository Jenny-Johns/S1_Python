x = int(input("Enter the limit: "))
names = []
count = 0
print("Enter", x,  "first names:")
for i in range(0, x):
    s = input()
    names.append(s)
print(names)
for i in names:
    for j in i:
        if j == "a":
            count = count+1
print("The number of occurrences of a:", count)

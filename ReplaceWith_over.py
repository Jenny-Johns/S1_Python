# for values greater than 100,store  'over' #
li = []
a = int(input("Enter the size of the list:"))
for i in range(a):
    v = int(input("Enter the integer:"))
    li.append(v)
print("The list is:", li)
for i in range(a):
    if li[i] > 100:
        li[i] = "over"
print("The list after replacing :", li)
# sum of elements in a list #

list1 = []
li = int(input("Enter the limit of list: "))
for i in range(0, li, 1):
    element = int(input("Enter the element: "))
    list1.append(element)
print("The list is :", list1)
x = len(list1)
print("Length of the list", x)
s = 0
for i in range(x):
    s = s+list1[i]
print("sum of elements in the list is:", s)

# even numbers removed list
list1 = []
newlist = []
li = int(input("Enter the limit of list: "))
for i in range(0, li, 1):
    element = int(input("Enter the element: "))
    list1.append(element)
print("The list is :", list1)
for i in range(len(list1)):
    if list1[i] % 2 == 0:
        continue
    else:
        newlist.append(list1[i])
print("The new list after removing even numbers:", newlist)

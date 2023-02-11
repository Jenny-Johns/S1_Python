# list comprehensions #
li = int(input("Enter the size of the list:"))
list1 = []
list2 = []
for i in range(li):
    v = int(input("Enter the integer: "))
    list1.append(v)
print("First list: ", list1)
list2 = [list1[i] for i in range(li) if list1[i] >= 0]
print("List of positive numbers:", list2)

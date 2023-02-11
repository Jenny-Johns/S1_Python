# Two list comparison #
l1 = []
l2 = []
s1 = 0
s2 = 0
n1 = int(input("Enter the size of first list: "))
print("Enter some integers for list 1: ")
for i in range(n1):
    n = int(input())
    l1.append(n)
n2 = int(input("Enter the size of second list: "))
print("Enter some integers for list 2: ")
for i in range(n2):
    m = int(input())
    l2.append(m)
print("List 1 :", l1)
print("List 2 :", l2)
if len(l1) == len(l2):
    print("List are of same length.\nLength:", len(l1))
else:
    print("Lists are not of the same length.")
for j in range(n1):
    s1 = s1+l1[j]
for k in range(n2):
    s2 = s2+l2[k]
if s1 == s2:
    print("Sum of values in both list are same.\nSum:", s1)
else:
    print("Sum of values in both list are not same.\nList1 sum:{}\nList2 sum:{}".format(s1, s2))
x = set(l1)
y = set(l2)
z = x.intersection(y)
if z == 0:
    print("No common values")
else:
    print("common values are:", z)

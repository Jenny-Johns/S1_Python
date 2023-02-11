# length of the largest word in the list #
lis = []
li = int(input("Enter the size of the list: "))
for i in range(li):
    w = str(input("Enter the word: "))
    lis.append(w)
print(lis)
t = lis[1]
m = len(lis[1])
for i in range(li):
    if m < len(lis[i]):
        m = len(lis[i])
        t = lis[i]
    else:
        i = i+1
print("The largest word in the list is:", t)
print("Length :", m)

s = input("Enter the sentence : ").split()
a = {}
for i in s:
    if i in a:
        a[i] = a[i]+1
    else:
        a[i] = 1
for m, n in a.items():
    print(m, "", n, "times")

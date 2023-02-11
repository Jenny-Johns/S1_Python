# Replacing first character occurrence with '$'#
s = str(input("Enter a string:"))
f = s[0]
for i in s:
    if i == f:
        s = s.replace(i, "$")
        s = f+s[1:]
print("The new string is :", s)

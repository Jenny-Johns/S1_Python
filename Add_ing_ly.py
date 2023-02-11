# adding 'ing' or 'ly' #
s = str(input("Enter the string: "))
print("The string is :", s)
if s[-3:] == 'ing':
    print("New string :", s+"ly")
else:
    print("New string :", s+"ing")

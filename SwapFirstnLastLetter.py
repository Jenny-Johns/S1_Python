# first and last char interchange #
string = input("Enter the string:")
first = string[0]
last = string[-1]
n = last + string[1:-1] + first
print("new string is", n)

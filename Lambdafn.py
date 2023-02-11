# using lambda function

l = int(input("Enter the length of the rectangle:"))
b = int(input("Enter the breadth of the rectangle:"))
area = lambda l, b: l * b
print("Area of rectangle", area(l, b))
s = int(input("Enter the length of the square:"))
areas = lambda s: s * s
print("Area of square", areas(s))
ba = int(input("Enter the base of the triangle:"))
h = int(input("Enter the height of the triangle:"))
ar = lambda ba, h: 0.5 * ba * h
print("Area of triangle", ar(ba, h))

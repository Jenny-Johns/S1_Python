dict1 = {
   "Name": "Jenny",
   "DOB": "1/5/1999",
   "Course": "MCA"
}
print(dict1)
x = list(dict1.items())
x.sort()
print("Ascending Order is : ", x)
y = list(dict1.items())
y.sort(reverse=True)
print("Descending Order is : ", y)

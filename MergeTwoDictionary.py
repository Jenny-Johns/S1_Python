# merge two dictionary
dict1 = {
   "Name": "Jenny",
   "DOB": "1/5/1999",
   "Course": "MCA"
}
dict2 = {
   "College": "Amaljyothi",
   "Duration": "2year",
   "Sem": 1
}
print(dict1)
print(dict2)
dict3 = dict1.copy()
dict3.update(dict2)
print(dict3)

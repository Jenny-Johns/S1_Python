from datetime import date, timedelta
dt = date.today() + timedelta(5)
dt1 = date.today() - timedelta(5)
print('Current date:', date.today())
print('5 days from current date:', dt)
print('5 days before current date:', dt1)

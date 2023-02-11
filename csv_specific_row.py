import csv

#  specify the no.of columns to be displayed
columns_read = [0, 2]

# open csv file
with open("Book1.csv", 'r') as file:
    # create a csv reader
    reader = csv.reader(file)
    # fetching each line from csv file
    for row in reader:
        print([row[i] for i in columns_read])

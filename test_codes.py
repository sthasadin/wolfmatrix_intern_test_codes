import csv

file = open("csv-sample.csv")
reader = csv.reader(file)
rows = len(list(reader))

print(rows)

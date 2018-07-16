import csv

csvpath = "Resources/budget_data.csv"
with open('csvpath','r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        print(line)

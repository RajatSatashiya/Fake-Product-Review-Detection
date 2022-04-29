import csv


file = open("datasetSpam.csv")
reader = csv.reader(file)

for row in reader:
    if(row[0] == "Rajat Satashiya"):
        print(row)

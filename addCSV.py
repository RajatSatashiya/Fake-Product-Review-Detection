"""
import csv
import random
import names

f = open("datasetSpam.csv", "w")
headings = ["Username", "Total Reviews", "Flagged Reviews", "Year Joined"]

with open("datasetSpam.csv", "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(headings)
    for i in range (0,3000):
        print("done " + str(i))
        name = names.get_full_name()
        totalrev = random.randint(50,150)
        flagged = random.randint(5, 80)
        year = random.randint(2005, 2022)
        row = [name, totalrev, flagged, year]
        writer.writerow(row)    
"""

import csv

with open("chart.csv", "r") as file :
    rs = csv.reader(file)
    
    rows = list(rs)
    
    for row in rows:
        print(row)
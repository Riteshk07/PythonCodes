import csv

with open("chart.csv", "r") as file :
    rs = csv.reader(file)
    
    rows = list(rs)
    
    for row in rows:
       for col in row:
            print(col, end= " ")
       print() 
       
    col = len(rows[0])
    
    print("Number of column: ", col)
    
# csv - comma separated values

import csv 

with open ("chart.csv", "w", newline='') as file:
    fw = csv.writer(file)
    fw.writerow(["sr", "Name", "Collage"])
    
    n = int (input("how many records do want to enter: "))
    
    for i in range (n):
        sr = i+1
        name = input("Enter Student's Name: ")
        collage = input ("Collage Name: ")
        fw.writerow([sr, name, collage])
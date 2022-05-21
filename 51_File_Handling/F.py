# csv - comma separated values

import csv 

with open ("chart.csv", "w") as file:
    fw = csv.writer(file)
    fw.writerow(["sr", "Name", "Collage"])
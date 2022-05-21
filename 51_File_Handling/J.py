import csv 
with open ("data.csv", "w", newline='') as file:
    fw = csv.writer(file)
    fw.writerow(["sr", "Name", "Collage"])
    
    n = int (input("how many records do want to enter: "))
    
    for i in range (n):
        sr = i+1
        name = input("Enter Student's Name: ")
        collage = input ("Collage Name: ")
        fw.writerow([sr, name, collage])
        
with open("data.csv", "r") as Rfile :
    rs = csv.reader(Rfile)
    
    rows = list(rs)
    x = len(rows)
    print("Number of Rows: ", x)
    y =len(rows[0])
    print("Number of column: ", y)
    
    ch = 0
    for i in range(y):
        for j in rows:
            ch += len(j[i])
            
    print ("Number of Charecter: ", ch)
    
    
    
    
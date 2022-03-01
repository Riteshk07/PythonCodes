gender = input("Enter Your Gender: ")

while gender!="M":
    if gender == "F":
        break
    print("Incorrect Gender")
    gender = input("Enter Your Gender: ")
z = input("Enter Your Age: ")
Age=int(z) if z.isdigit() else ""

while Age=="":
    print("Please Enter Age only in Number")
    z = input("Enter Your Age: ")
    Age=int(z) if z.isdigit() else ""

while Age>250 or Age<0:
    print ("Invalid Age")
    print("Please Enter Age between 0 to 250 Years")
    z = input("Enter Your Age: ")
    Age=int(z) if z.isdigit() else ""
    while Age=="":
        print("Please Enter Age between 0 to 250 Years")
        z = input("Enter Your Age: ")
        Age=int(z) if z.isdigit() else ""

female="For Student\nNo Min balance, Interest 4 %" if Age<=22 else ("For Se. Citizen\nNo Min balance, Interest 12 %" if Age>=60 else  "For General\nMin balance 2000, Interest 8 %" )
male= "For Student\nMin balance 500, Interest 2 %"if Age<=22 else("For Se. Citizen\nMin balance 2000, Interest 11 %"if Age>=60 else "For General\nMin balance 5000, Interest 6 %" )

form = male if gender=="M" else(female if gender=="F" else "Enter Correct Gender")

print(form)
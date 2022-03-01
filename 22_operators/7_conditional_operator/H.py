x = input("Enter Your Gender: ")
t = input("Enter Your Age: ")

z=int(t) if t.isdigit() else ""
A = "" if type(z)==str or z>250 or z<0 else z 

female="Invalid Age" if type(A)==str else ("For Student\nNo Min balance, Interest 4 %" if A<=22 else ("For Se. Citizen\nNo Min balance, Interest 12 %" if A>=60 else  "For General\nMin balance 2000, Interest 8 %" ))
male= "Invalid Age" if type(A)==str else("For Student\nMin balance 500, Interest 2 %"if A<=22 else("For Se. Citizen\nMin balance 2000, Interest 11 %"if A>=60 else "For General\nMin balance 5000, Interest 6 %" ))

form = male if x=="M" else(female if x=="F" else "Enter Correct Gender")

print(form)
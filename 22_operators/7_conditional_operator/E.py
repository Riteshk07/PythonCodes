m= input("Enter marks: ")
y=int(m) if m.isdigit() else "Eneter Correct Marks" 

result= "Enter Correct Marks" if type(y)==str else"Enter correct Marks" if y<0 else("fail" if y<=33 else ("3rd division" if y<= 50 else ("Second Division" if y <=60 else ("First division" if y<=100 else "Enter correct marks"))))

print(result)
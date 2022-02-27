name = input("Enter Your Name: ")
mb = int(input("Min. Balnce: "))

x = input("Gender: ")
t = int(input("Age: "))
female= (8/100)*mb if mb>=2000 and t>22 else ((12/100)*mb if t>60 else(4/100)*mb if t<=22 else "Your Account has minimum Balance")

male= f"Minimum balance 5000 and age t>22 and 12% intrest is {(6/100)*mb}" if mb>=5000 and t>22 else (f"Minimum balance 2000 and age age>60 and 11% intrest is: {(11/100)*mb}" if t>60 and mb>=2000 else(f"Minimum balance 500 and age t<=22 and 12% intrest is: {(2/100)*mb}" if t<=22 and mb>=500 else "You are not eligible to open acccount"))

interest = male if x=="M" else female

print(interest)
def ageNum():
    z = input("Enter Your Age: ")
    A=int(z) if z.isdigit() else ""
    return A
gender = input("Enter Your Gender: ")
while gender!="M":
    if gender == "F":
        break
    print("Incorrect Gender")
    gender = input("Enter Your Gender: ")

age = ageNum()
while age=="" or age>250 or age<0:
    print("Please Enter correct Age")
    age= ageNum()

cheq = input('Do you want a cheque book...?(Y/N): ')
while cheq!="Y":
    if cheq == "N":
        break
    print("Invalid Input")
    cheq = input('Do you want a cheque book...?(Y/N): ')
charge = 0
if cheq == 'Y':
    charge = 500

if gender == 'M':
    if age <= 22:
        print(f'Minimum Balance: {500+charge} and Interest Rate: 2%')
    elif age <= 60:
        print(f'Minimum Balance: {5000+charge} and Interest Rate: 6%')
    else:
        print(f'Minimum Balance: {2000+charge} and Interest Rate: 11%')
else:
    if age <= 22:
        print(f'Minimum Balance: {0+charge} and Interest Rate: 4%')
    elif age <= 60:
        print(f'Minimum Balance: {2000+charge} and Interest Rate: 8%')
    else:
        print(f'Minimum Balance: {0+charge} and Interest Rate: 12%')
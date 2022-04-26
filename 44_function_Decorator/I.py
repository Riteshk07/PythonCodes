
def account ():
    global count 
    global accNum
    count =0
    accNum = 0
    name=input("Enter Your Name: ")
    Age = int (input ("Enter Your Age: "))
    acctype = input ("Enter Saving/Current ")
    aCard = input ("Do you have Aadhar Card ? Y/N : ")
    if aCard == "Y":
        aNum = int (input ("Enter Aadhar Number: "))
    elif aCard == "N":
        aNum = None
    accNum +=1
    acInfo = open("AccountInfo.txt","a")

     
    LA = input("Login Here: ")
    psw = input ("Enter password: ")
    acInfo = open("AccountInfo.txt","a")
    if LA==acInfo.readline() and psw==acInfo.readline():
        print(name)
        print (Age)

    acInfo.close()


account()
    
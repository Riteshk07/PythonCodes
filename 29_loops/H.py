x= input("Do you want to calculate? (y/n): ")

while x=="y":
    y = input("What do You want? Choose one (+,-,*,/,%): ")
    i = int(input("Value 1: "))
    j = int(input("Value 2: "))
    if y=="+":
        print(i,y,j,"=",i+j)
    elif y=="-":
        print(i,y,j,"=",i-j)
    elif y=="*":
        print(i,y,j,"=",i*j)
    elif y=="/":
        print(i,y,j,"=",i/j)
    elif y=="%":
        print(i,y,j,"=",i%j)
    else:
        print("invalid Input")
    x= input("Do you want to calculate? (y/n): ")
print("Thank You...!")
n=int (input("Enter Number: "))
a=0
for i in range (1,n+1):
    for j in range(i):
        print((a+i)-(j+1),end=" ")
        a+=1
    print()
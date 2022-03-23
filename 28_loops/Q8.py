n=int (input("Enter Number: "))
a=1
for i in range (1,n+1):
    for j in range(i,0,-1):
        if a%2==1:
            print(a,end =" ")
        a+=2
    print()
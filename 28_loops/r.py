n=int (input("Enter Number: "))
a=ord('A')
c=int(n*(n+1)/2)
for i in range (1,n+1):
    for j in range(i,0,-1):
        print(chr(a+c-1),end =" ")
        c-=1
    print()
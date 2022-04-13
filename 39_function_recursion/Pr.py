def pro1(n):
    global i
    if n>0:
        i+=1
        print(i , end=" " ) 
        pro1(n-1)

def pro2(n):
    if n>0:
        pro1(x) 
        print()
        pro2(n-1)
x=int(input("Enter: "))
i=0
pro2(x)
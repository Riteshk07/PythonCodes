def pro1(n):
    global i
    if n>0:
        i+=1 
        if n%2==0:
            print(chr(j+i-1), end=" " )
        else:
            print(i, end=" " )
        pro1(n-1)

def pro2(n):
    if n>0:
        pro1(x) 
        print()
        pro2(n-1)
x=int(input("Enter: "))
i=0
j = ord("A")
pro2(x)
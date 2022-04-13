def pro1(n):
    global j
    if n>0:
        j -=1
        print(chr(j-1), end=" " )
        pro1(n-1)
        


def pro2(n):
    if n>0:
        pro1(x) 
        print()
        pro2(n-1)
x=int(input("Enter: "))

j = (ord("A"))+x**2
pro2(x)
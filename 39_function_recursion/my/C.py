def pro1(n):
    global i
    if n>0:
        pro1(n-1)
        i-=1
        print(chr(i) ,end=" ")


def pro2(a):
    if a>0:
        pro2(a-1)
        pro1(x)
        print()

x=int (input("Enter: "))
i = (ord("A"))+(x**2)
pro2(x)
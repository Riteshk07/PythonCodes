def pro1(n):
    if n>0:
        pro1(n-1)
        print("*" ,end=" ")


def pro2(a):
    if a>0:
        pro2(a-1)
        pro1(x)
        print()

x=int (input("Enter: "))
pro2(x)
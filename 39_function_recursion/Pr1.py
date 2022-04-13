def pro1(n):
    global i
    if n>0:
        print(chr(j+i), end=" " )
        i+=1 
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
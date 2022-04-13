def pro(n):
    if n>0:
        pro(n-1)
        print(1)
    print(5)

pro(3)
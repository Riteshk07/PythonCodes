n = 5
a = 1
for i in range(1, n+1):
    
    for j in range(n+1, 0, -1):
        if j > i:
            print(" ", end=" ")
        else:
            print(a, end=" ")
            a += 1
    print()
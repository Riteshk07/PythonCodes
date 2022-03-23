n=3 
n= int(n*(n+1/2))

a = ord('A')

for i in range(n+a,a-1,-1):
    for j in range (i-a):
        print(chr(i)+" "*(n-a) )
        n -=1

for i in x:
    if i%2==1:
        print(i)

print("############################\nSolution 1: ")
n= int(input("Enter Number: "))

ch = ord('A')
num= 0
for i in range(n):
    for j in range(n):
        num+=1 
        if ch%2==1:
            print(chr(ch), end= " ")
        else:
            print(num , end=" ")
        ch+=1
    print()
print("############################\nSolution 2: ")
ch = ord('A')
num= 0
for i in range(n):
    for j in range(n):
        num+=1 
        if ch%2==0:
            print(chr(ch), end= " ")
        else:
            print(num , end=" ")
        ch+=1
    print()
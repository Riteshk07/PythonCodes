print("############################\nSolution 1: ")
n= int(input("Enter Number: "))

ch = ord('A')
num= 1
for i in range(n):
    if ch%2==1:
        print(chr(ch),i+2, end= " ")
    else:
        print(num ,chr(ch+i+1),end=" ")
    ch+=3
    num += 3
    print()
    
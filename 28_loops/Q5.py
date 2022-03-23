n= int (input("Enter Number: "))
a=1
for i in range (1,n+1):
   if a%2==1: 
    print(f"{a} "*i)
    a+=2


'''
1 
3 3
5 5 5
7 7 7 7
9 9 9 9 9
'''
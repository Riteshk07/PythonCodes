n= int (input("Enter Number: "))

for i in range(1,n+1):
    for j in range(i,0,-1):
        print(j,end=" ")

    print ()


'''
1
2 1       
3 2 1     
4 3 2 1   
5 4 3 2 1 
'''
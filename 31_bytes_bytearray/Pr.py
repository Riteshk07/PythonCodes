t = (9,8,7,6,5,4,3,2,1,0)
b= bytearray(t)

x = True
while x :
    x= False
    for i in range(len(b)-1):
        if b[i]>b[i+1]:
            x= True
            s= b[i]
            b[i]= b[i+1]
            b[i+1]=s

for j in b :
    print(j,end = " ")


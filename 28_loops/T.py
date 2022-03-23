from ast import Break


x=[1,2,3,4,5,6,7,8,9]
a = False
for i in x:
    if i%2==1:
        a=True
        Break

print(a)
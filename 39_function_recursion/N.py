def fib(n):
    global num1,num2
    if n==0:
        print(0)
    if n>0:
        fib(n-1)
        if n>=2:
            s = num1 + num2
            num1, num2 = num2, s
            print(s)
        else: 
            print(1)
num1,num2= 0,1

x= int(input("Enter: "))
fib(x) 

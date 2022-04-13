def fib(n):
    global num1,num2
    if n>0:
        fib(n-1)
        if n < 3:
            print(1)
        if n>=3:
            the_sum = num1 + num2
            num1, num2 = num2, the_sum
            print(the_sum)
num1,num2= 1,1

x= int(input("Enter: "))
fib(x)

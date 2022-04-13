def fib(n):
    if n < 3:
        return 1
    if n>0:
        fib(n-1)
        print(fib(n - 1) + fib(n - 2))
x= int(input("Enter : "))
fib(x)
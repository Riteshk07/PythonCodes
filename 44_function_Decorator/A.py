def greet():
    print("hello ji")

# a decorator function 
def decorate_greet(func):
    def xgreet():
        print("Hi")
        func()
    return xgreet

x = decorate_greet(greet)
x()
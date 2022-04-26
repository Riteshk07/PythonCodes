# a decorator function 
def decorate_greet(func):
    def xgreet():
        print("Hi")
        func()
    return xgreet
    
@decorate_greet
def greet():
    print("hello ji")

greet()
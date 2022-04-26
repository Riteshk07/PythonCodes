def greet():
    print("hello ji")

# a decorator function 
def decorate_greet(func):
    def xgreet():
        print("Hi")
        func()
    return xgreet

greet= decorate_greet(greet)

greet()

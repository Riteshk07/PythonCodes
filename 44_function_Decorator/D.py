from decorators import do_twice

@do_twice
def greet():
    print("Hello ji")

greet()
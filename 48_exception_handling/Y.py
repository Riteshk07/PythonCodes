try:
    x=12/0
except(ArithmeticError):
    print("This is Arithmetic")
except(ZeroDivisionError):
    print("zero division")
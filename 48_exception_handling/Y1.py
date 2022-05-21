try:
    x=12/0
except(ArithmeticError ,ZeroDivisionError) as msg:
    print("This is Arithmetic" , msg)

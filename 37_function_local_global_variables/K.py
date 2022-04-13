def pro1():
    x = 9
    global x
    x = 8
    print(x)

# SyntaxError: name 'x' is assigned to before global declaration

def pro():
    x = 90

    def info():
        w = 10

    def aaa():
        e = 34

    print(locals())

pro()

# {'x': 90, 'info': <function pro.<locals>.info at 0x000001530520A200>, 'aaa': <function pro.<locals>.aaa at 0x000001530520A290>}
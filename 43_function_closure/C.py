def aaa():
    print('inside aaa')

    x = 45

    #closure function
    #1. is a nested function
    #2. accessing variable declared in enclosing scope(check line 11)
    #3. and returned from the enclosing scope (check line 13)
    def bbb():
        print(x)

    return bbb
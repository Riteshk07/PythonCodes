def pro():
    print('-------- 1')

    #UnboundLocalError: local variable 'info' referenced before assignment
    info()

    #defined a nested function: info
    def info():
        print('----- A')

    print('-------- 2')

    


pro()
def pro():
    print('-------- 1')

    #defined a nested function: info
    def info():
        print('----- A')

    print('-------- 2')


info()

# NameError: name 'info' is not defined

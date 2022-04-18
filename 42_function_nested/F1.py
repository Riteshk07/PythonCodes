def pro():
    print('Y')
    def info():
        print('G')
    print('T')

def aaa():
    pro()
    info()  # NameError: name 'info' is not defined


aaa()

# nested function is not accessible outside of it's enclosing function...
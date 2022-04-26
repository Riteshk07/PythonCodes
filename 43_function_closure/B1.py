def aaa():
    print('~~~~~')
    a = 90
    def bbb():
        nonlocal a
        a = 78
        print(a)

    bbb()
    print(a)

aaa()
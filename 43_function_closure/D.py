def aaa():
    print('inside aaa')

    x = 45

    def bbb():
        print(x)

    return bbb


z = aaa()

z()
def aaa():
    print('A')
    y = 12 / 0
    print('A1')

def bbb():
    print('B')
    aaa()
    print('B1')

def ccc():
    print('C')
    bbb()
    print('C1')

ccc()
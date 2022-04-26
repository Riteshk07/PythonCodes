def aaa(n):
    print('~~~~~')
    a = 90
    def bbb():
        print(a, n)
    print(locals())

aaa(12)
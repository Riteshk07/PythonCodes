def pro():
    x = 90
    def aaa():
        print(1)
    print(locals())
    def bbb():
        print(2)
    print(locals())
    
pro()
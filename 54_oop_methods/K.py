class A:
    y = 9

    def __init__(self, x):
        self.x = x

    def process(self):
        z = 5
        # print(x)  not ok
        # print(y)  not ok
        # print(z)
        # print(self.x)
        # print(self.y)
        # print(self.z)  not ok
        
        # not ok
        # print(cls.x)
        # print(cls.y)
        # print(cls.z)



a = A(7)

a.process()
class A:
    y = 11

    def __init__(self, x):
        self.x = x

    @classmethod
    def process(cls):
        z = 5
        # print(x)  not ok
        # print(y)  # not ok
        # print(z)
        # print(self.x)   not ok
        # print(self.y) not ok
        # print(self.z)  not ok
        
        # print(cls.x)  not ok
        # print(cls.y)
        # print(cls.z)  not ok


A.process()
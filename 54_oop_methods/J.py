class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius
    
    def calcArea(self):
        print(self.__dict__)

    def calcPerimeter(self):
        return 2 * self.pi * self.radius
    
    @classmethod
    def getPi(cls):    
        print(cls.__dict__)

a = Circle(10)
b = Circle(100)

print(a.calcPerimeter())
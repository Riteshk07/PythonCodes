class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius
    
    def calcArea(self):
        print(self)

    
    @classmethod
    def getPi(cls):    
        print(cls)

a = Circle(10)
b = Circle(100)

a.calcArea()
a.getPi()
b.calcArea()
b.getPi()
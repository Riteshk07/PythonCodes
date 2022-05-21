class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    # instance level method
    def calcArea(self):
        print(self.pi * self.radius * self.radius)


a = Circle(10)
b = Circle(100)

a.calcArea()
b.calcArea()
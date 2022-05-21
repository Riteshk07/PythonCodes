class Circle:
    # class level member variable
    pi = 3.14

    def __init__(self, radius):
        # instance level variable member
        self.radius = radius

    # instance level method
    def calcArea(self):
        print(self.pi * self.radius * self.radius)

    @classmethod
    def getPi(cls):
        return Circle.pi
        # return cls.pi

a = Circle(10)
b = Circle(100)

print(Circle.getPi())
print(a.getPi())
print(b.getPi())
print(a.pi)
print(b.pi)
print(Circle.pi)

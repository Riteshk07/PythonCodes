class Circle:
    # class level member variable
    pi = 3.14

    def __init__(self, radius):
        # instance level variable member
        self.radius = radius

    # instance level method
    def calcArea(self):
        print(self.pi * self.radius * self.radius)

    # class level method
    @classmethod
    def getPi(cls):
        return Circle.pi
        # return cls.pi

    # TypeError: Circle.defineCircle() takes 0 positional arguments but 1 was given
    def defineCircle():
        print( '''
                a round plane figure whose boundary (the circumference) consists of 
                points equidistant from a fixed point (the centre).
                ''')

a = Circle(10)
b = Circle(100)

a.defineCircle()
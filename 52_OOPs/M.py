class Student:
    #class level variable common to all the objects of student class
    city = 'Jabalpur'

    def __init__(self, name, age, college):
        # instance level variable
        self.name = name
        self.age = age
        self.college = college 

a = Student('om', 23, 'Global')
b = Student('ram', 21, 'SRIT')

print(a.__dict__)
print(b.__dict__)

print(a.name, a.age, a.college, a.city)
print(b.name, b.age, b.college, b.city)
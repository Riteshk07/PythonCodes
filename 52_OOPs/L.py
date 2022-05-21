class Student:
    city = 'Jabalpur'

    def __init__(self, name, age, college):
        self.name = name
        self.age = age
        self.college = college 

a = Student('om', 23, 'Global')
b = Student('ram', 21, 'SRIT')

print(a.__dict__)
print(b.__dict__)

print(Student.__dict__)
class Student:
    def __init__(self, name, age, college):
        self.name = name
        self.age = age
        self.college = college 

a = Student('om', 23, 'Global')

print(a.__dict__)
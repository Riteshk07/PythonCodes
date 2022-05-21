class Student:
    def __init__(self):
        self.name = 'om'
        self.age = 12
        self.college = 'JEC'


a = Student()
b = Student()
c = Student()

print(a.__dict__)
print(b.__dict__)
print(c.__dict__)
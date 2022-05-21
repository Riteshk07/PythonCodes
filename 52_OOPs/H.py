class Student:
    pass


a = Student()

a.name = 'om'
a.age = 12

print(a.__dict__)

b = Student()

b.name = 'ram'
b.college = 'JEC'

print(b.__dict__)
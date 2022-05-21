class Person:
    pass

class Student(Person):
    name = 'golu'

    def login():
        pass

print(Student.__bases__)
print(Person.__bases__)
print(object.__bases__)
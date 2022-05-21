class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info():
        print(name, age)

x = Student('om', 12)

x.show_info()


# TypeError: Student.show_info() takes 0 positional arguments but 1 was given
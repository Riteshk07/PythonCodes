class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(self.name, self.age)

x = Student('om', 12)
y = Student('ram', 17)

# Student.show_info()

Student.show_info(x)
Student.show_info(y)
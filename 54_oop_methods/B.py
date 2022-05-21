class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(self.name, self.age)

x = Student('om', 12)

# show_info()    # NameError: name 'show_info' is not defined

# Student.show_info()  # TypeError: Student.show_info() missing 1 required positional argument: 'self'

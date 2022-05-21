class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(name, age)

x = Student('om', 12)

x.show_info()

# NameError: name 'name' is not defined
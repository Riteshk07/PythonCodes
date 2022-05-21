class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # method show_info is accessing instance level properties that is 
    # why must be defined as an instance level method
    # instance level method that is why must be self parameterized 
    def show_info(self):
        print(self.name, self.age)

x = Student('om', 12)

x.show_info()

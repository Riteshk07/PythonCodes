class Employee:
    # class level property company         
    company = 'TCS'

    def __init__(self, name, salary, experience):
        # instance level properties for employee objects
        # each employee object will have it's own copy of instance variable
        # so that you can store diffrent employee records in diffrent employee objects
        # you can say that one object for each employee record
        self.name = name
        self.salary =salary
        self.experience = experience


a = Employee('gajanan', 23000, 3)
b = Employee('chandragupt', 45000, 5)

# company property is common to all the objects of employee class
print(a.name, a.salary, a.experience, a.company)
print(b.name, b.salary, b.experience, b.company)

# you can access only class level variables company using class Name Employee
# you can't access instance level variables using class Employee
print(Employee.company)
# print(Employee.name)   # AttributeError: type object 'Employee' has no attribute 'name'
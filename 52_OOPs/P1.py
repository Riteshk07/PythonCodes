class Employee:
    company = 'TCS'

    def __init__(self, name, salary, experience):
        self.name = name
        self.salary =salary
        self.experience = experience


a = Employee('gajanan', 2)

print(a)

print(a.name)

print(a.salary)
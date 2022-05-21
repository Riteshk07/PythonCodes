class Employee:
    company = 'TCS'

    def __init__(self, name, salary, experience):
        print(self)
        print(name)
        print(salary)
        print(experience)


a = Employee('gajanan', 23000, 2)

print(a)

print(a.name)
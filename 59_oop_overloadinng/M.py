
class Employee:
    def __init__ (self, name, SPD):
        self.name = name
        self.SPD = SPD

class TimeSheet:
    def __init__(self, name, days):
        self.name = name
        self.days = days

e =  Employee("Raj", 1000)
t = TimeSheet("Raj", 5)

salary = e*t

# TypeError: unsupported operand type(s) for *: 'Employee' and 'TimeSheet'
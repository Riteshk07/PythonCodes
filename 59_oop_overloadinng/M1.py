class Employee:
    def __init__ (self, name, SPD):
        self.name = name
        self.SPD = SPD
    def __mul__(self, val):
        return self.SPD * val.days

class TimeSheet:
    def __init__(self, name, days):
        self.name = name
        self.days = days
    def __mul__(self, val):
        return self.days * val.SPD

e =  Employee("Raj", 1000)
t = TimeSheet("Raj", 5)

s1 = e*t
s2 = t*e
print(s1)
print(s2)

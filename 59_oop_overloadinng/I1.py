class Account :
    def __init__(self, balance):
        self.balance = balance
    def __str__(self):
        return str(self.balance)
    def __add__(self, val):
        return self.balance + val.balance


x= Account(20)
y= Account(30)

print(x)
print(y)


print(x+y)

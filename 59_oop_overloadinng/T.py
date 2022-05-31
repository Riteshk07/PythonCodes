class Account:
    def __init__(self, balance):
        self.balance = balance

    def __str__(self):
        return str(self.balance)
    def __add__(self, val):
        return self.balance + val.balance

x = Account(70)
y = Account(60)

print(x+y)
print(x.__add__(y))
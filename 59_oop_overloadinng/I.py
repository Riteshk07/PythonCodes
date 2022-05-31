class Account :
    def __init__(self, balance):
        self.balance = balance
    def __str__(self):
        return str(self.balance)
x= Account(20)
y= Account(30)

print(x)
print(y)


print(x+y)

# TypeError: unsupported operand type(s) for +: 'Account' and 'Account'
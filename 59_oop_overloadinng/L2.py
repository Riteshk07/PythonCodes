class Account :
    def __init__(self, balance):
        self.balance = balance
    def __str__(self):
        return str(self.balance)
    def __add__(self, val):
        temp = self.balance + val.balance
        return Account(temp)

x= Account(20)
y= Account(30)
z= Account(50)
t = Account(60)
u = Account(40)
print(x+y+z+t+u)

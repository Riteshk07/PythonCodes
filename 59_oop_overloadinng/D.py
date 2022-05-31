class A :
    @classmethod 
    def pro(cls):
        print("hi")

    def pro(self):
        print("hello")

# A.pro()
# TypeError: A.pro() missing 1 required positional argument: 'self'

x= A()
x.pro()

print(A.__dict__)
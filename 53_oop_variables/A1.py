class A:
    # class level variable
    x = 9

    def __init__(self):
        print(A.x)

a = A()


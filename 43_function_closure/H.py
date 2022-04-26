def xyz(n):
    m = 89

    def pqr():
        print(n, m)
    
    return pqr

t = xyz(100)

t()

# print(t.__closure__)
print(t.__closure__[0])
print(t.__closure__[1])
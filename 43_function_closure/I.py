def xyz(n):
    m = 89

    def pqr():
        print(n, m)
    
    return pqr

t = xyz(100)

t()

print('++++++++++++++++') 
print(t.__closure__[0].cell_contents)
print(t.__closure__[1].cell_contents)
def xyz(n):
    m = 89

    def pqr():

        o=55
        def aaa():
            print (m,n,o)
        return aaa
    
    return pqr

t = xyz(100)

t()()

print('++++++++++++++++') 
print(t().__closure__[0].cell_contents)
print(t().__closure__[1].cell_contents)
print(t().__closure__[2].cell_contents)
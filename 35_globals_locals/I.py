x = 33

def pro():


    def info():
        pass
    
    print(locals())
pro.locals[x] =22

pro()
print(globals())

i = 0

def pro():
    global i
    print(i)
    pro()    
    i += 1


pro()
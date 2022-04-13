i = 0

def pro():
    global i
    print(i)    
    i += 1
    if i < 5:
        pro()


pro()
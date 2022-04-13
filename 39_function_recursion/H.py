i = 0

def pro():
    global i        
    i += 1
    if i < 5:
        pro()    
    print(i)


pro()
i = 0

def pro():
    global i
    print(i)
    i += 1
    pro()


pro()
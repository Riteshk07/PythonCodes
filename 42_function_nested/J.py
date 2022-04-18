def pro():
    print(1)
    def info():
        print(2)
    print(3)
    return info


x = pro()

x()

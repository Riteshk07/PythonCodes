def pro():
    def info():
        return 44
    return info

x = pro()

y = x()

print(y)
x = [5, 15, 25]

y = [88, 99]

print(x, id(x))

x.insert(1, y)

print(x, id(x))
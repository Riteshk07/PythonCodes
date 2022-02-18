# set is mutable

x = {45, 34, 12, 67}

print(x, id(x))

x.add(102)

print(x, id(x))

x.remove(45)

print(x, id(x))
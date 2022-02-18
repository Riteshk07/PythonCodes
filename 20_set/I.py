# set tcan grow

x = {45, 34, 12, 67}

print(x, id(x))

# x.append(78)   # AttributeError: 'set' object has no attribute 'append'

x.add(78)

print(x, id(x))
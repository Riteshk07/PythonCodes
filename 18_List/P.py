x=[23,54,65]
print(x,id(x[2]))
del x[2]
print(x)
x.insert(2,33)
x.pop()
print(x)

x.insert(9,78)

print(x,id(x[2]))
del x[2]
print(x)
x.insert(6,65)
print(id(x[2]))

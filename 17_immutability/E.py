x = True

y = x

print(id(x), x)
print(id(y), y)

x = False

print(id(x), x)
print(id(y), y)
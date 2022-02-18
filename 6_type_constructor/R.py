x = '0o34'

print(x, type(x))

# y = int(x)              # ValueError: invalid literal for int() with base 10: '0o34'
y = int(x, 8)              

print(y, type(y))
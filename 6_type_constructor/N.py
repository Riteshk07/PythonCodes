# x = '12'
x = '1a2'

y = int(x)    # ValueError: invalid literal for int() with base 10: '1a2'

print(x, type(x))
print(y, type(y))
x = '0x34'

print(x, type(x))

# y = int(x)                # ValueError: invalid literal for int() with base 10: '0x34'

y = int(x, 16)

print(y, type(y))
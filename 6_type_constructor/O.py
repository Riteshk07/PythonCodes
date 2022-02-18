x = '0b111'    # string constant

print(x, type(x))

y = int(x)              # ValueError: invalid literal for int() with base 10: '0b111'

print(y, type(y))
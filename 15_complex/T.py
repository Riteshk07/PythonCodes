# x = complex('2')
# x = complex('a')   # ValueError: complex() arg is a malformed string
x = complex('a', 'b')

print(x)

print(type(x))
a = '23'
b = '12'

x = complex(a, b)     # TypeError: complex() can't take second arg if first is a string

print(x)

print(type(x))
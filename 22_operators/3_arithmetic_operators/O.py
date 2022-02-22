# x = 'om'
x = '12'

y = 2

# z = x + y  # TypeError: can only concatenate str (not "int") to str

z = int(x) + y

print(z, type(z))
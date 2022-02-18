# x = 34.76

# x = 2+3j         # TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'

# x = '12'

# x = '12.45'        # ValueError: invalid literal for int() with base 10: '12.45'  

# x = True
# x = False

x = 'False'         # ValueError: invalid literal for int() with base 10: 'False'

y = int(x)

print(y)
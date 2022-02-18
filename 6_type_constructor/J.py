x = '2+3j'
y = 3+2j

# z = x + y   # TypeError: can only concatenate str (not "complex") to str

z = complex(x) + y


print(z)

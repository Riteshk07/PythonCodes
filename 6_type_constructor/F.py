x = '2.3'    # x is a str variable

y = 1.2      # y is a float variable


# z = x + y    # TypeError: can only concatenate str (not "float") to str

z = float(x) + y    # it is possible if x is converted to a float value 

print(z, type(z))



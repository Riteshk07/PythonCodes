x = '2.3'    # x is a str variable

y = 1.2      # y is a float variable


# z = x + y    # TypeError: can only concatenate str (not "float") to str

# z = float(x) + y    # it is possible if x is converted to a float value 

z = x + str(y)        # it is also possible if y is converted to str value


print(z, type(z))



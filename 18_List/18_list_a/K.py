x = [12,13,14]

print(x, id(x))

# x[3] = 52          # IndexError: list assignment index out of range

x[1] = 99

print(x, id(x))


# list object is mutable ... 
# list can grow and shrink ...
# you can change value of an index location ...
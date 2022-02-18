x = [12,13,14]

print(x, id(x))

# x[3] = 52          # IndexError: list assignment index out of range

x.append(52)

print(x, id(x))


# list can grow
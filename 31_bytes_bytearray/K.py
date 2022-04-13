# x = list(3)  # TypeError: 'int' object is not iterable

# x = tuple(3)   #TypeError: 'int' object is not iterable

# x = set(3)   #TypeError: 'int' object is not iterable

x = bytes(3)

print(x[0])
print(x[1])
print(x[2])

print(len(x))
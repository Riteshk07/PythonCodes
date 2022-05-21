file = open('eknath.txt', 'r')

# val = file.read()
val = file.read(5)
print(val)
val = file.read(5)
print(val)
val = file.read(5)
print(val)

file.close()
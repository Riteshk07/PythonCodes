file = open('eknath.txt', 'r')

print(file.tell())
val = file.read(5)
print(val)

print(file.tell())
val = file.read(5)
print(val)

print(file.tell())
val = file.read(5)
print(val)

file.close()
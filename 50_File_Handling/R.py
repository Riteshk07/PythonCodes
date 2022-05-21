file = open ("eknath.txt", "r")

lines = file.readlines()

print(type(lines))

for l in lines :
    print(l)

file.close()
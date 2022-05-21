import random

file = open('eknath.txt', 'r')

lines = file.readlines()

print(type(lines))

for line in lines:
    val = random.randrange(0,3)    
    if val == 0:
        print(line.upper())
    elif val == 1:
        print(line.title())
    elif val == 2:
        print(line.capitalize())
    
file.close()
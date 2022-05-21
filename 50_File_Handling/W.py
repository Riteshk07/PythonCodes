#new
with open('eknath.txt', 'r') as file:
    print(file.readline())
    print(file.readline())
    print(file.readline())
    print(file.closed)    

print(file.closed)

#old:

# file = open('eknath.txt', 'r')

# print(file.readline())
# print(file.readline())
# print(file.readline())

# print(file.closed)

# file.close()

# print(file.closed)
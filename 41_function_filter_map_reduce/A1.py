x = [57, 31, 2, 45, 24, 78, 97, 28, 42]

y = []

def iseven(n):
    return n % 2 == 0

n = filter(iseven, x)

print(n)
print(type(n))
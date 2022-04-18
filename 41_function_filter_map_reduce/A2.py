x = [57, 31, 2, 45, 24, 78, 97, 28, 42]

def iseven(n):
    return n % 2 == 0

n = filter(iseven, x)

m = list(n)

print(x)
print(m)
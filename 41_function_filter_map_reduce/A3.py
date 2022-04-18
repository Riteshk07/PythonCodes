x = [52, 38, 3, 44, 29, 78, 97, 28, 42]

# def iseven(n):
#     return n % 2 == 0

iseven = lambda n : n % 2 == 0

n = filter(iseven, x)

m = list(n)

print(x)
print(m)
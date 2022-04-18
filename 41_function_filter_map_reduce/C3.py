x = [2,4,6,8]

# def square(n):
#     return n * n

square = lambda n : n * n

z = map(square, x)

y = list(z)

print(y)
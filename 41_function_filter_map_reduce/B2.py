x = [52, 38, 3, 44, 29, 78, 97, 28, 42]

# def gt40(i):
#     return i > 40

gt40 = lambda i : i > 40

n = filter(gt40, x)

m = list(n)

print(m)
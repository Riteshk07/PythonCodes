x = [52, 38, 3, 44, 29, 78, 97, 28, 42]
 

n = filter(lambda n : n % 2 == 0, x)

m = list(n)

print(x)
print(m)
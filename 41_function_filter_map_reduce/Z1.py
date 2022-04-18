x=[(1,2,3),(4,5,6),(7,8,9)]

y = list(map(sum, x))

print(y)

z = list(map(lambda a: a[0]+a[1]+a[2], x))

print(z)
x = {'name': 'om', 'email': 'om@gmail.com', 'password': 12334}

y = {'degree': 'BTech', 'branch': 'CS'}

print(x, id(x))
print(y)

x.update(y)

print(x, id(x))
print(y)
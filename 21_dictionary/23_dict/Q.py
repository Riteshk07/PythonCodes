x = {'name': 'om', 'email': 'om@gmail.com', 'password': 12334}

y = {'name': 'ganesh', 'degree': 'BTech', 'branch': 'CS'}

print(x, id(x))
print(y)

x.update(y)

print(x, id(x))
print(y)
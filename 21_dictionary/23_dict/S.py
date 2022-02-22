x = {'name': 'om', 'email': 'om@gmail.com', 'password': 12334}

y = {'degree': 'BTech', 'branch': 'CS'}

print(x)

# x.extend(y)    # AttributeError: 'dict' object has no attribute 'extend'

z = x + y  

print(x)
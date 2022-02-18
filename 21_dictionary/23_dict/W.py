x = {'name': 'om', 'email': 'om@gmail.com', 'password': 12334}

print(x)

print(x.popitem())
print(x.popitem())
print(x.popitem())
print(x.popitem())    # KeyError: 'popitem(): dictionary is empty'

print(x)
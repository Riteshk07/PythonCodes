x = {'name': 'om', 'email': 'om@gmail.com', 'password': 12334}

# print(x['name'])
# print(x['email'])
# print(x['password'])

# print(x['college'])   # KeyError: 'college

print(x.get('name'))
print(x.get('email'))
print(x.get('password'))
print(x.get('college'))
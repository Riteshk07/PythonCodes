x = {'name': 'om', 'email': 'om@gmail.com', 'password': 12334}

print(x)

# x.pop('email', 'name', 'password')

x.pop('college')    # KeyError: 'college'

print(x)
x = {'name': 'om', 'email': 'om@gmail.com', 'password': 12334}

print(x, id(x))

x['name'] = 'mohan'

print(x, id(x))


# duplicate keys not allowed 
# old value will be replaced by the new value
# if you attempt to assign to an existing key record
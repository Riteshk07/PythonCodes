# dictionary is mutable thus not reusable 

x = {'name': 'om', 'email': 'om@gmail.com', 'password': 12334} 

y = {'name': 'om', 'email': 'om@gmail.com', 'password': 12334} 

print(x is y)

print(id(x))
print(id(y))
print('A')

x = {'name':'om', 'age':12}

key = input('Enter one of the key(name, age): ')

try:
    print(x[key])
except NameError:
    print('problem')

print('B')
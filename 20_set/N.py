# unlike list and tuple the set does not support + operator to add 2 sets

x = {1,2,3}
y = {4,5}

z = x + y    # TypeError: unsupported operand type(s) for +: 'set' and 'set'

print(x)
print(y)
print(z)
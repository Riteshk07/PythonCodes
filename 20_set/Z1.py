x= {45,89,47,22}
y=(54,87,98,32)

# z=x|y           # TypeError: unsupported operand type(s) for |: 'set' and 'tuple'
z= x.union(y)     #   OK

print(z)
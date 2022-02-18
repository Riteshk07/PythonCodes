
# tuple can't grow

x = (45, 67, 89)

# x.append(44)        # AttributeError: 'tuple' object has no attribute 'append'
# x.insert(1, 22)       # AttributeError: 'tuple' object has no attribute 'insert'
# x.extend(34)            #AttributeError: 'tuple' object has no attribute 'extend'

print(x)
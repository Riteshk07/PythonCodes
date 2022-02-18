x = {34, 12, 4, 5}

# a = 99
# a = [99,88]  # TypeError: unhashable type: 'list'
a = (99,88)
# a = {99,88}  # TypeError: unhashable type: 'set'

x.add(a)

print(x)
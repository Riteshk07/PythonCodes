# x = [23,56,78]
x = (23,56,78)

y = x.find(56)    # AttributeError: 'list' object has no attribute 'find'
                  # AttributeError: 'tuple' object has no attribute 'find'  

print(y)
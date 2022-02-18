'''index

Returns the index of the first occurrence of the specified list item.
'''

x=(45,7,6,66,74,12,31)
print(x, type(x))
            # Required. Any valid type. ValueError is raised if item is not in the list.
# y=x.index()         # TypeError: index expected at least 1 argument, got 0
# y=x.index(1)       # ValueError: tuple.index(x): x not in tuple
y=x.index(7)

print(y)


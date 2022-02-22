x = {'a': 4, 'b': 3, 'c': 2, 'd': 1}


y=sorted(x.items(), key=lambda x: x[1])
print(y)

import operator
y=sorted(x.items(), key=operator.itemgetter(1))
print(y)
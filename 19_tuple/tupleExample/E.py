'''count
Description
Returns the number of times the specified item appears in the list.'''

x=(45,7,6,66,74,12,6,6,31)
print(x, type(x))
            # Required. Any valid type.
# y=x.count()     # TypeError: tuple.count() takes exactly one argument (0 given)
# y=x.count(9)    # if diffrent value you givin. The result is always 0 <class 'int'>
y=x.count(6)    #result = 3

print(y,type(y))
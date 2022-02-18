'''min funtion

Returns the smallest item from a collection.'''

# x=(45,7,6,66,74,12,6,6,31)
# print(x, type(x))

# x=('A','a','B','b')
# x=('aanchal','aakansha','aabhash')        # Result --> aabhash
# x=([1,2,9],[2,1,9],[1,1,200],[2,1,1])     # Result --> [1, 1, 200]
x=(str([1,2,9]),str([2,1,9]),str([1,1,200]),str([2,1,1]))   # Result --> [1, 1, 200]
print(x, type(x))
y=min(x)
print(y)
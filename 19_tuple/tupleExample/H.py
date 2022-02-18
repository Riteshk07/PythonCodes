'''max function
Description
Returns the largest item in an iterable or the largest of two or more arguments.'''


# x=(45,7,6,66,74,12,6,6,31)
# print(x, type(x))

# x=('A','a','B','b')     # Result --> b
# x=('aarti','aakansha','aabhash')        # Result --> aarti
# x=([1,2,9],[2,1,9],[1,1,200],[2,1,1])     # Result --> [2 ,1, 9]
x=(str([1,2,9]),str([2,1,9]),str([1,1,200]),str([2,1,1]))   # Result --> [2, 1, 9]
print(x, type(x))
y=max(x)
print(y)
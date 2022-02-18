x = 3.21

# y = 3.210000000001
y = 3.210000000000001
print("x is y ? ",x is y)
print("id of x: ",id(x))
print("id of y: ",id(y))
print (f"value of x: {x}\nvalue of y: {y}\n")

y = 3.2100000000000001              # In this Example 
print("x is y ? ",x is y)           # id of x and y is matching.
print("id of x: ",id(x))            # the result value of x and y is same
print("id of y: ",id(y))            # we need to print or convert a float number to 15 decimal place string 
print (f"value of x: {x}\nvalue of y: {y}\n")   # even if the result has many trailing 0s

y = round(3.210000000000000001,2)   # In this Example 
print("x is y ? ",x is y)           # id of x and y is not matching.
print("id of x: ",id(x))            # but the result value of x and y is same.
print("id of y: ",id(y))
print (f"value of x: {x}\nvalue of y: {y}")

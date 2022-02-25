# find largest number:

x=int(input("Enter First number: "))
y=int(input("Enter Second number: "))
z=int(input("Enter Third number: "))

result= x if x>y and x>z else (z if z>y else y)
print(result)
# x=(12,45)+(8,10)     # this is the way it was intended

x=12,5+(4,15)            # too ambiguous for the interpreter
# TypeError: unsupported operand type(s) for +: 'int' and 'tuple'

print(x,type(x))
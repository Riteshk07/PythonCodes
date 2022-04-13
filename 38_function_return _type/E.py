# input: 2 3 +
# input: 'om' 'kumar' +
# input: 'om' 3 *
# input: 17 0 /
# input: 2 3 %

# python is a dynamically typed language 
# the parameter type and the return type is not fixed
# you can pass different types of argument as demonstrated
# and also expect to get different types of values in return 

def calc(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b
    else:
        print('invalid operator!!')

x = input('Enter +, -, * or /: ')
y = eval(input('Enter first value: '))
z = eval(input('Enter second value: '))

res = calc(y, z, x)

print(res)
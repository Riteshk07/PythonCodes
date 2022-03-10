x = int(input('Enter first number: '))
y = int(input('Enter second number: '))

if x == y:
    print(f'both x:{x} and y:{y} are same')
elif x > y:
    print(f'x:{x} is greater')
else:
    print(f'y:{y} is greater')
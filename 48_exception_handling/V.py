print(1)

try:
    print(2)

    n = int(input('Enter a number: '))

    print(3)

    x = [2, 0, 3]

    print(4)

    print(12/x[n])

    print(5)

    y = {'name':'om', 'age':12}

    print(6)

    key = input('Type on of the key name/age: ')

    print(7)

    print(y[key])

    print(8)
except (ValueError, ZeroDivisionError, IndexError) as msg:
    print('problem ~~', msg)
except KeyError as msg:
    print('problem ##', msg)

print(9)

# input values: om, 0, 1, 2, 3, 
print(1)

try:
    print(2)
    n = int(input('Enter a number: '))
    print(3)
    x = [2, 0, 3]
    print(4)
    y = 12 / x[n]
    print(5)
    print(y)
    print('Essential code...')
except ValueError:
    print('VE ------')
    print('Essential code...')
except IndexError:
    print('IE ------')
    print('Essential code...')

print(6)


# input value: om, 0, 1
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
except IndexError:
    print('IE ------')

print(6)


# input value: om
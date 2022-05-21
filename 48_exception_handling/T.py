print(1)

try:
    print(2)

    n = int(input('Enter a number: '))

    print(3)

    x = [2, 0, 3]

    print(4)

    print(12/x[n])

    print(5)
except (ValueError, ZeroDivisionError, IndexError):
    print('problem --#')


print(6)

# input values: om, 0, 1, 2, 3
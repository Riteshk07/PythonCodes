print(1)

try:
    print(2)

    n = int(input('Enter a number: '))

    print(3)

    x = [2, 0, 3]

    print(4)

    print(12/x[n])

    print(5)   
except BaseException:
    print('All In one solution')    
except ValueError as msg:      
    print('problem VE', msg)
except ZeroDivisionError as msg:
    print('problem ZDE', msg)
except IndexError as msg:
    print('problem IE', msg)


print(6)
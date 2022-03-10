marks = int(input('Enter marks(%): '))

if marks < 0 or marks > 100:
    print('Invalid Input')
else: 
    if marks < 33:
        print('Fail')
    elif marks < 45:
        print('T')
    elif marks < 60:
        print('S')
    elif marks < 75:
        print('F')
    else:
        print('D')

marks = int(input('Enter marks(%): '))

if marks >= 0 and marks <= 100:
    elif marks < 33:
        print('Fail')
    elif marks < 45:
        print('T')
    elif marks < 60:
        print('S')
    elif marks < 75:
        print('F')
    else:
        print('D')
else: 
    print('Invalid Input')
    

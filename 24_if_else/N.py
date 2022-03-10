gender = input('Enter gender(m/f): ')
age = int(input('Enter Age: '))

if age >= 1 and age <= 100:
    if gender == 'm':
        if age <= 22:
            print('MB: 500 and IR: 2%')
        elif age <= 60:
            print('MB: 5000 and IR: 6%')
        else:
            print('MB: 2000 and IR: 11%')
    elif gender == 'f':
        if age <= 22:
            print('MB: 0 and IR: 4%')
        elif age <= 60:
            print('MB: 2000 and IR: 8%')
        else:
            print('MB: 0 and IR: 12%')
    else:
        print('Invalid Gender ... ')
else:
    print('Invalid Age...')
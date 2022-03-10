gender = input('Enter gender(m/f): ')
age = int(input('Enter Age: '))
chq = input('Do you want a cheque book...?(y/n): ')


if chq == 'y' or chq == 'n':
    
    charge = 0
    if chq == 'y':
        charge = 500

    if age >= 1 and age <= 100:
        if gender == 'm':
            if age <= 22:
                print(f'MB: {500+charge} and IR: 2%')
            elif age <= 60:
                print(f'MB: {5000+charge} and IR: 6%')
            else:
                print(f'MB: {2000+charge} and IR: 11%')
        elif gender == 'f':
            if age <= 22:
                print(f'MB: {0+charge} and IR: 4%')
            elif age <= 60:
                print(f'MB: {2000+charge} and IR: 8%')
            else:
                print(f'MB: {0+charge} and IR: 12%')
        else:
            print('Invalid Gender ... ')
    else:
        print('Invalid Age...')
else:
    print('Invalid cheque book value...')
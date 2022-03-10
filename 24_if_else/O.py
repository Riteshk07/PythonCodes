gender = input('Enter gender(m/f): ')
age = int(input('Enter Age: '))
chq = input('Do you want a cheque book...?(y/n): ')

if chq == 'y' or chq == 'n':
    if age >= 1 and age <= 100:
        if gender == 'm':
            if age <= 22:
                print('MB: %d and IR: 2%%' %(500 if chq == 'n' else 500+500))
            elif age <= 60:
                print('MB: %d and IR: 6%%' %(5000 if chq == 'n' else 5000+500))
            else:
                print('MB: %d and IR: 11%%' %(2000 if chq == 'n' else 2000+500))
        elif gender == 'f':
            if age <= 22:
                print('MB: {} and IR: 4%'.format(0 if chq == 'n' else 0+500))
            elif age <= 60:
                print('MB: {} and IR: 8%'.format(2000 if chq == 'n' else 2000+500))
            else:
                print('MB: {} and IR: 12%'.format(0 if chq == 'n' else 0+500))
        else:
            print('Invalid Gender ... ')
    else:
        print('Invalid Age...')
else:
    print('Invalid cheque book value...')
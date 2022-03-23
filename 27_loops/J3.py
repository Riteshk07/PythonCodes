x = [45, 23, 89, 56, 102, 8, 92, 34, 67, 8, 72, 8, 34, 23, 8]

n = int(input('Enter a number: '))

flag = False

for i in x:
    if i == n:
        print('-')
        flag = True
        break
        

if flag:
    print('Found')
else:
    print('Not Found')


# enter: 33, 8
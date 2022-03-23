xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

n = int(input('Enter a number: '))

for i in range(n):
    for j in range(n):
        print('even' if (i+j)%2==0 else 'odd', end=' ')
    print()    
#input: n = 3

#output
'''
* * *
  * *
    *
'''

n = int(input('Enter a number: '))

for i in range(n):
    for j in range(n):
        if i == j or i < j:
            print('*', end='')
        else:
            print(' ', end='')
    print()

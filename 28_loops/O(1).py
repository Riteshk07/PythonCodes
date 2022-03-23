#input: n = 3

#output
'''
6
5 4
3 2 1
'''

n = int(input('Enter a number: '))

c = int(n * (n+1) / 2)

for i in range(n):
    for j in range(i+1):
        print(c, end=' ')
        c -= 1
    print()
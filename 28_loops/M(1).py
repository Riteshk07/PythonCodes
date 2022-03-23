#input: n = 3

#output
'''
1
2 3
4 5 6
'''

n = int(input('Enter a number: '))

c = 1

for i in range(n):
    for j in range(i+1):
        print(c, end='')
        c += 1
    print()
#input: n = 3

#output
'''
1 1 1
2 2 2
3 3 3
'''

n = int(input('Enter a number: '))

for i in range(n):
    for j in range(n):
        print(i+1, end=' ')
    print()


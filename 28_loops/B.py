#input: n = 3

#output
'''
3 3 3
2 2 2
1 1 1
'''

n = int(input('Enter a number: '))

for i in range(n):
    print(f'{n-i} '*n)

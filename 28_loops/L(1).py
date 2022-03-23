#input: n = 3

#output
'''
1
2 2
3 3 3
'''

n = int(input('Enter a number: '))

for i in range(1, n+1):
    print(f'{i}'*i)
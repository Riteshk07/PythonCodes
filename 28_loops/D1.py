#input: n = 3

#output
'''
C C C
B B B
A A A
'''

n = int(input('Enter a number: '))

for i in range(n-1, -1, -1):
        print(f'{chr(i+65)} '*n)
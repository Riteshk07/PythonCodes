#input: n = 3

#output
'''
A A A
B B B
C C C
'''

n = int(input('Enter a number: '))

for i in range(n):
    print(f'{chr(i+65)} '*n)
    
#input: n = 3

#output
'''
C C C
B B B
A A A
'''

n = int(input('Enter a number: '))

for i in range(n+65-1, 64, -1):
    for j in range(n):
        print(chr(i), end=' ')
    print()
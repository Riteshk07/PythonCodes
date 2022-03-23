#input: n = 3

#output
'''
F
E D
C B A
'''

n = int(input('Enter a number: '))

start = ord('A') + int(n * (n+1) / 2) - 1

for i in range(n):
    for j in range(i+1):
        print(chr(start), end='')
        start -= 1
    print()
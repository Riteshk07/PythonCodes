#input: n = 3

#output
'''
A
B C
D E F
'''

n = int(input('Enter a number: '))

c = ord('A')

for i in range(n):
    for j in range(i+1):
        print(chr(c), end=' ')
        c += 1
    print()
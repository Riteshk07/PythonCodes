#input: n = 3

#output
'''
A A A
B B B
C C C
'''

n = int(input('Enter a number: '))

for i in range(65, 65+n):
    for j in range(n):
        print(chr(i),end=' ')
    print()
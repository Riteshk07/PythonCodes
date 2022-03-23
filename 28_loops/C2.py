#input: n = 3

#output
'''
A A A
B B B
C C C
'''

n = int(input('Enter a number: '))

y = ord('A')

for i in range(n):
    print(f'{chr(i+y)} '*n)
    
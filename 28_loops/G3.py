#input: n = 3

#output
'''
1 B 3
D 3 C
4 D 5
'''

n = int(input('Enter a number: '))

x = 1
y = ord('A')

for i in range(n):
    for j in range(n):
        if x % 2 == 0:
            print(x, end=' ')
        else:
            print(chr(y), end=' ')
        
        x += 1
        y += 1

    print()
    

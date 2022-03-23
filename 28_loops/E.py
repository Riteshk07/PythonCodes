#input: n = 3

#output
'''
1 A 2
B 3 C
4 D 5
'''

n = int(input('Enter a number: '))

x = 1
y = ord('A')
t = 1

for i in range(n):
    for j in range(n):
        if t % 2 == 1:
            print(x, end=' ')
            x += 1
        else:
            print(chr(y), end=' ')
            y += 1  

        t += 1 
    print()
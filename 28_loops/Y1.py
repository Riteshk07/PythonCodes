n = int(input('Enter a number: '))

ch = ord('A')

for i in range(n):
    for j in range(n):
        print('even' if ch%2==0 else 'odd', end=' ')
        ch += 1 
    print() 
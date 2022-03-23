n = int(input('Enter a number: '))

ch = ord('A')

for i in range(n):
    for j in range(n):
        print(ch, end=' ')
        ch += 1 
    print() 
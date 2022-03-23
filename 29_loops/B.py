n = int(input('Enter a number: '))

x = ord('A')
y = ord('a')

while n:
    if n % 2 == 1:
        print(chr(x))
    else:
        print(chr(y))
    x += 1
    y += 1
    n -= 1
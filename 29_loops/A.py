n = int(input('Enter a number: '))

start = ord('a') + n - 1

while n:
    print(chr(start), end=' ')
    start -= 1
    n -= 1

n = int(input('Enter a number: '))

end = ord('a')

while n:
    print(chr(end+n-1), end=' ')
    n -= 1

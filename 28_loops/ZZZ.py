start = ord('a')
end = ord('z')

x = ord(input('Enter a-z: '))

if x>=start and x<end:
    print(f'i/p:{chr(x)} and o/p:{chr(x+1)}')
elif x==end:
    print('a')
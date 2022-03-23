# x = [34, 56, 78, 90, 23, 45, 120, 27, 13, 8]
x = [23, 45, 27, 13]

max_even = None

for i in x:
    if i % 2 == 0:
        if max_even == None:
            max_even = i
        elif max_even < i:
            max_even = i

if max_even != None:
    print(f'{max_even} is the largest even number in the given list')
else:
    print('No Max even number found...')


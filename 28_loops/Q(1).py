# x = [44, 68, 12, 8, 24]
x = [44, 68, 12, 7, 24]
x = [44, 68, 12, 7, 24, 37, 12, 51]

# check whether an odd record is contained in the list

print('does the given list contain an odd record? ')

for i in x:
    if i % 2 == 1:
        print('yes')
    else:
        print('no')


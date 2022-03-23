# x = [44, 68, 12, 7, 24, 37, 12, 51]
x = [44, 68, 12]

# check whether an odd record is contained in the list

print('does the given list contain an odd record? ')

flag = False

for i in x:
    if i % 2 == 1:
        flag = True 
        break

if flag:
    print('yes')
else:
    print('no')


x = [44, 68, 12, 7, 24, 37, 12, 51]
# x = [44, 68, 12]

# check whether an odd record is contained in the list

print('does the given list contain an odd record? ')

for i in x:
    if i % 2 == 1:
        print('yes') 
        break
else:
    print('no')

# else block will also execute if for loop does not end abnormally(using break)...


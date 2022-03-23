x = 'vishwajeet'

t = 0

for i in x:
    if t % 2 == 0:
        print(i.upper(), end='')
    else:
        print(i, end='')

    t = t + 1
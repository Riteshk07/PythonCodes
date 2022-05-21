import os

fname = input('Enter file name: ')

if os.path.isfile(fname):
    print(f'{fname} exists')
    with open(fname, 'r') as file:
        for line in file:
            print(line)
else:
    print(f'{fname} does not exist')
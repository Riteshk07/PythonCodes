#input: n = 3

#output
'''
* * *
  * *
    *
'''

n = int(input('Enter a number: '))

for i in range(n):
    print(' '*i, '*'*(n-i), sep='')
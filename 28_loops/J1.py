#input: n = 3

#output
'''
    *
  * *
* * *
'''

n = int(input('Enter a number: '))

for i in range(1,n+1):
    print(' '*(n-i) + '*'*i)
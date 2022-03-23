#input: n = 3

#output
'''
*
* *
* * *
'''

n = int(input('Enter a number: '))

#Case 2:
for i in range(1,n+1):
    print('* ' * i)


# Case 1:
'''
for i in range(n):
    print('* ' * (i+1))
'''
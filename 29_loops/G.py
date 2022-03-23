import time

print('start work')

f = input('work start?(y/n): ')

while f == 'y':
    print('Keep on working')
    time.sleep(2)
    f = input('work continue?(y/n): ')

print('end work')

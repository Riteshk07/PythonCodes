file = open('yamaraj.txt', 'w')

y = ('my friend is a good cricketer', 'his name is gagan shrivas', 'gagan is my best friend')

# file.write(y)
file.writelines(y)

file.close()
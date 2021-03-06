# Different ways to test multiple
# flags at once in Python
x, y, z = 0, 1, 0

if x == 1 and y == 1 and z == 1:
    print('passed')
else:
    print("failed")

if 1 in (x, y, z):
    print('passed')

# These only test for truthiness:
if x or y or z:
    print('passed')

if any((x, y, z)):
    print('passed')
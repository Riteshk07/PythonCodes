def aaa():
    print('inside aaa')

    def bbb():
        print('inside bbb')

    return bbb


z1 = aaa()
z2 = aaa()

del aaa

print('------')
z1()
z2()

print('###########')

print(z1)
print(z2)
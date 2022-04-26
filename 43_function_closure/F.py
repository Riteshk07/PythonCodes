def aaa(n):
    print('inside aaa')

    def bbb():
        print(n)

    return bbb


z1 = aaa(23)
z2 = aaa(49)

del aaa

print('------')
z1()
z2()

print('###########')

print(z1)
print(z2)
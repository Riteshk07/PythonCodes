file = open ("eknath.txt", "w")

a = [True, False, True]
b= [2.34,4.55,6.88]


#file.writelines(a)
#file.writelines(b)

file.writelines([str(i) for i in a])
file.writelines([str(i) for i in b])
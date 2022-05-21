file = open('eknath.txt', 'w')

# a = [23, 45, 67]
# a = ['om','ram','shyam']
# a = {'om-','ram-','shyam-'}
a = {'name': 'mohan', 'age': 34}

file.writelines(a)

file.close();
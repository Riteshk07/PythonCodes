x1=eval(input("Enter value 1: "))
x2=eval(input("Enter value 2: "))
x3=eval(input("Enter value 3: "))
x4=eval(input("Enter value 4: "))
x5=eval(input("Enter value 5: "))
x6=eval(input("Enter value 6: "))
x7=eval(input("Enter value 7: "))
x8=eval(input("Enter value 8: "))
x9=eval(input("Enter value 9: "))

list1=[]

list1.append(x1)	# Adds at the end of list
list1.append(x2)
list1.append(x3)
list1.append(x4)
list1.append(x5)
list1.append(x6)
list1.append(x7)
list1.append(x8)
list1.append(x9)

list1.sort()     	 # sort the list
list1.reverse()		# reverse the list		

print(list1)
print(f'Total value: {sum(list1)}')
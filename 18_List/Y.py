my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

n=[ ]
for i in range(len(my_list)):
    if my_list[i]not in n:
        n.append(my_list[i])

print("The list with unique elements only:")
print(my_list)
print(n)
lst = [7,8,9,11,13]
l = len(lst)
for i in range(l//2):
    t= lst[i]
    lst[i]=lst [l-1-i]
    lst[l-1-i]=t
print(lst)
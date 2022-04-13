def eveAccur(itera):
    x=[]
    for i in  itera:
        if i not in x:
            x.append(i)
    for j in x:
        c=0
        for k in itera:
            if j==k:
                c+=1
        print(f"{j} -->  {c}")


a = 1, 2, 3, 2, 4, 6, 2, 7, 2, 8, 9
# duplicates = tup.count(2)
# print(duplicates)    # outputs: 4
eveAccur(a)



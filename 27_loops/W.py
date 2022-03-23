x = [12, 56, 78, 34, 12, 45, 29, 76, 83, 34, 6, 12, 56, 12, 34, 78]

count = 0

for i in x:
    for j in x:
        if i == j:
            count += 1
    
    print(i, '-', count)

    count = 0
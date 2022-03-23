x = [34, 56, 78, 23, 45, 120, 27, 13, 8]

count = 0

for i in x:
    if i % 2 == 0:
        count += 1

print(f'{count} even records found...')
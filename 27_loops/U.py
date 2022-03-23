x = [34, 56, 78, 90, 23, 45, 120, 27, 13, 8]

even_count = 0
odd_count = 0

for i in x:
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f'{even_count} even records found and {odd_count} odd records found...')
x = ["ram", "ganesh", "om", "mohan", "vikram", "vikas"]

for i in x:
    l = len(i)

    if l % 2 == 1:
        # print(i.capitalize())
        continue

    print(i.upper())

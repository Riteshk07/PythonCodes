file = open ("spiderman.png", "rb")

bs = file.read()

# print(bs)

file.close()

file = open ("drStrange.png", "wb")

file.write(bs)

file.close()

# r, w, a, x, rb, wb
file= open("pratap.txt", "w")       # open() is a function

print(file.closed)

file.close()        # <file-object>.close() is a method

print(file.closed)
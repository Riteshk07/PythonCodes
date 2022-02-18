# x= bin(23)                   #result in binary type str

# x= bin(True)                # YOU CAN PASS BOOL VALUE
# x= bin(False)

# x= bin(3.43)                # TypeError: 'float' object cannot be interpreted as an integer

# x= bin(0o45)                # YOU CAN PASS oct num
# x= bin(0x12)                  ## YOU CAN PASS hex num
# x= bin(0b10111)              # You can pass binary number

# x= bin("name")              #TypeError: 'str' object cannot be interpreted as an integer
# x= bin("45")                # you can't pass an integer inside in string because 'str' object cannot be interpreted as an integer

# x= bin(int(input()))        # now you can pass integer inside in string.
x= bin(eval(input()))       # now you can pass integer (binary octal decimal hexal) and bool inside in string.

print(x,type(x))
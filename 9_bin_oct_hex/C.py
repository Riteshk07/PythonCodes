# x= hex(23)                   #result in hexal type str

# x= hex(True)                # YOU CAN PASS BOOL VALUE
# x= hex(False)

# x= hex(3.43)                # TypeError: 'float' object cannot be interpreted as an integer

# x= hex(0o45)                # YOU CAN PASS oct num
# x= hex(0x12)                  ## YOU CAN PASS hex num
# x= hex(0b10111)              # You can pass binary number

# x= hex("name")              #TypeError: 'str' object cannot be interpreted as an integer
# x= hex("45")                # you can't pass an integer inside in string because 'str' object cannot be interpreted as an integer

# x= hex(int(input()))        # now you can pass integer inside in string.
x= hex(eval(input()))       # now you can pass integer (binary octal decimal hexal) and bool inside in string.

print(x,type(x))
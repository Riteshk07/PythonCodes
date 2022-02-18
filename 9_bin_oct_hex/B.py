# x= oct(23)                   #result in octal type str

# x= oct(True)                # YOU CAN PASS BOOL VALUE
# x= oct(False)

# x= oct(3.43)                # TypeError: 'float' object cannot be interpreted as an integer

# x= oct(0o45)                # YOU CAN PASS oct num
# x= oct(0x12)                  ## YOU CAN PASS hex num
# x= oct(0b10111)              # You can pass binary number

# x= oct("name")              #TypeError: 'str' object cannot be interpreted as an integer
# x= oct("45")                # you can't pass an integer inside in string because 'str' object cannot be interpreted as an integer

# x= oct(int(input()))        # now you can pass integer inside in string.
x= oct(eval(input()))       # now you can pass integer (binary octal decimal hexal) and bool inside in string..

print(x,type(x))
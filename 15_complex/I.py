# x = 0b111+0b11j    # SyntaxError: invalid binary literal
# x = 0b111+0o11j    # SyntaxError: invalid octal literal
x = 0b111+0x11j      # SyntaxError: invalid hexadecimal literal

print(x)

print(type(x))

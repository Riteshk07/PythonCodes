# print(10 < 10.01)  # 10 is less than 10.01 -> True

# print(10 < 10+1j)  # 10 is less than 10+1j -> Error -> TypeError: '<' not supported between instances of 'int' and 'complex'

# print(10 == 10+0j)  # 10 is equal to 10+0j -> True

# print(10 <= 10+0j)  # Error

print(10 != 10+0j)  # 10 is equal to 10+0j -> True

# < > <= and >= are not supported between int and complex
# == and != are supported between int and complex
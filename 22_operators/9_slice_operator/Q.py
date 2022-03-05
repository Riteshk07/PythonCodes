x = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# y = x[-2:-6:0]    # start-index: -2 and end-index: -6 and step: 0
y = x[2:6:0]    # start-index: -2 and end-index: -6 and step: 0

print(y)

# ValueError: slice step cannot be zero
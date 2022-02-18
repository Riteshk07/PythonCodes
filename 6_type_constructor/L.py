# x="3E8"         # ValueError: invalid literal for int() with base 10: '3E8'
# y=int(x)        # because it is show as floting point variable 
x=3E8
y=3.6E9

a="111_111_11"    # We can use (_) inside an integer
b=int(a)
print(f"{x}\n{y}\n{b} ")
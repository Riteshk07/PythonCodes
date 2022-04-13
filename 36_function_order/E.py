def pro1():
    print('A')
    pro2()
    print('B')

pro1()

def pro2():
    print('C')

# NameError: name 'pro2' is not defined. Did you mean: 'pro1'?

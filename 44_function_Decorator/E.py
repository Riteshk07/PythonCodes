from decorators import do_twice

@do_twice
def greet(name):
    print(f"Hello {name}")

greet("Ritesh")

'''
line 7, in <module>
    greet("Ritesh")
TypeError: do_twice.<locals>.wrapper_do_twice() takes 0 positional arguments but 1 was given
'''
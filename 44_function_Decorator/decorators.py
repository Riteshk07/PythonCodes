def do_twice(func):
    def new_greet():
        func()
        func()
    return new_greet


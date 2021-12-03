import functools

def star(f):
    @functools.wraps(f)
    def inner1(*args, **kwargs):
        print("*" * 30)
        f(*args, **kwargs)
        print("*" * 30)
    return inner1

def percent(f):
    @functools.wraps(f)
    def inner2(*args, **kwargs):
        print("%" * 30)
        f(*args, **kwargs)
        print("%" * 30)
    return inner2

@star
@percent
def printer(msg):
    print(msg)

printer("Hello, Signal!")

# inner1 if didn't use @functools.wraps(f)
print(f"printer.__name__ = {printer.__name__}")


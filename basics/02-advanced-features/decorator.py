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
print("=" * 50)
def log(text):
    def decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            print(f"{text} {f.__name__}")
            return f(*args, **kwargs)
        return wrapper
    return decorator

dec = log("execute")
print(f"dec = {dec}")
print(f"dec.__name__ = {dec.__name__}")
wrapper = dec(print)
print(f"wrapper = {wrapper}")
print(f"wrapper.__name__ = {wrapper.__name__}")
print(f"wrapper('Hello, Signal!') = {wrapper('Hello, Signal!')}")

from contextlib import contextmanager

@contextmanager
def managed_file(name):
    try:
        f = open(name, 'a')
        yield f
    finally:
        f.close

with managed_file('signal.txt') as f:
    f.write('hello, signal!\n')

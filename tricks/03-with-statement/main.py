"""
application of with statement
  1. with open('hello.txt', 'w') as f:
         f.write("hello, world!")
  2. some_lock = threadng.Lock()
         with some_lock:
             # Do something...
  3. Supporting with in object
"""
class ManagedFile:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.file = open(self.name, 'a')
        return self.file

    def __exit__(self, exc_type, _exc_val, exc_tb):
        if self.file:
            self.file.close()

with ManagedFile('hello.txt') as f:
    f.write('hello, world!\n')

try:
    print('try...')
    r = int('a')
    print(f"result = {r}")
except ValueError as e:
    print(f"ValueError: {e}")
except ZeroDivisionError as e:
    print(f"ZeroDivisionError: {e}")
finally:
    print('finally...')
print('END')
print("=" * 50)

def foo(s):
    n = int(s)
    if n == 0:
        raise ValueError(f'invalid value: {n}')
        return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError')
        raise
bar()

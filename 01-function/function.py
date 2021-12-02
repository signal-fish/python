def f1(a, b, c=0, *args, **kwargs):
    print(f"a = {a}, b = {b}, c = {c}, args = {args}, kwargs = {kwargs}")

f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
args, kwargs = (1, 2, 3, 4), {'d': 99, 'x': '#'}
f1(*args, **kwargs)  # !important

print("=" * 30)

# If there are no variable arguments, * must be added as a special separator.
def f2(a, b, c=0, *, d, **kwargs):
    print(f"a = {a}, b = {b}, c = {c}, d = {d}, kwargs = {kwargs}")

args, kwargs = (1, 2, 3), {'d': 99, 'x': '#'}
f2(*args, **kwargs)

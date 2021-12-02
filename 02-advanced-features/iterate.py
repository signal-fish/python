from collections.abc import Iterable

d = {'a':1, 'b':2}
for key in d:
    print(key)

for v in d.values():
    print(v)

for k, v in d.items():
    print(k, v)

for ch in "AB":
    print(ch)

for i, v in enumerate(['A', 'B']):
    print(i, v)

for x, y in [(1, 1), (2, 4)]:
    print(x, y)

print(isinstance('abc', Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance((1, ), Iterable))
print(isinstance({'a':1}, Iterable))
print(isinstance(123, Iterable))

import os

print([x*x for x in range(1, 6)])

print([m+n for m in 'AB' for n in 'XY'])

print([x for x in range(1, 11) if x % 2 == 0])

print([d for d in os.listdir('.')])

import functools

# Built-in functions that read iterables and return single values

all([1, 2, 3])
all([1, 0, 3])
all([])

any([1, 2, 3])
any([1, 0, 3])
any([0, 0.0])
any([])
g = (n for n in [0, 0.0, 7, 8])
any(g)
next(g)

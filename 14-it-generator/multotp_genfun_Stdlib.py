import itertools
import operator

# Generator functions that expand each input item into multiple output
# items.

ct = itertools.count()
next(ct)
next(ct), next(ct), next(ct)

list(itertools.islice(itertools.count(1, .3), 3))

cy = itertools.cycle('ABC')
next(cy)
list(itertools.islice(cy, 7))

rp = itertools.repeat(7)
next(rp), next(rp)
list(itertools.repeat(8, 4))

list(map(operator.mul, range(11), itertools.repeat(5)))
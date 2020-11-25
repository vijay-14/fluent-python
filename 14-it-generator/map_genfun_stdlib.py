import itertools
import operator

# Mapping generator functions in standard library

sample = [5, 4, 2, 8, 7, 6, 3, 0, 9, 1]

# itertools.accumulate examples
list(itertools.accumulate(sample))

list(itertools.accumulate(sample, min))

list(itertools.accumulate(sample, max))

list(itertools.accumulate(sample, operator.mul))

list(itertools.accumulate(range(1, 11), operator.mul))

# enumerate, map, starmap examples
list(enumerate('albatroz', 1))

list(map(operator.mul, range(11), range(11)))

list(map(operator.mul, range(11), [2, 4, 8]))

list(map(lambda a, b: (a, b), range(11), [2, 4, 8]))

list(itertools.starmap(operator.mul, enumerate('albatroz', 1)))

sample = [5, 4, 2, 8, 7, 6, 3, 0, 9, 1]

list(itertools.starmap(lambda a, b: b/a,
enumerate(itertools.accumulate(sample), 1)))
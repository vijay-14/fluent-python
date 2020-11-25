import itertools

#  Merging generator functions examples

list(itertools.chain('ABC', range(2)))

list(itertools.chain(enumerate('ABC')))

list(itertools.chain.from_iterable(enumerate('ABC')))

list(zip('ABC', range(5)))

list(zip('ABC', range(5), [10, 20, 30, 40]))

list(itertools.zip_longest('ABC', range(5)))

list(itertools.zip_longest('ABC', range(5), fillvalue='?'))






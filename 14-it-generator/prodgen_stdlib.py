import itertools

# itertools.product generator examples

list(itertools.product('ABC', range(2)))

suits = 'spades hearts diamonds clubs'.split()
list(itertools.product('AK', suits))

list(itertools.product('ABC'))

list(itertools.product('ABC', repeat=2))

list(itertools.product(range(2), repeat=3))

rows = itertools.product('AB', range(2), repeat=2)
for row in rows: print(row)





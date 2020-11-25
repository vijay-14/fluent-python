import itertools

# The combinations, combinations_with_replacement and permutations generator
# functions — together with product — are called the combinatoric generators in the
# itertools documentation page

list(itertools.combinations('ABC',2))

list(itertools.combinations_with_replacement('ABC', 2))

list(itertools.product('ABC', repeat=2))
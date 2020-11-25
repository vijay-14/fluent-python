import itertools

# Rearranging generator functions.

list(itertools.groupby('LLLLAAGGG'))

for char, group in itertools.groupby('LLLLAAAGG'):
    print(char, '->', list(group))

animals = ['duck', 'eagle', 'rat', 'giraffe', 'bear',
           'bat', 'dolphin', 'shark', 'lion']
animals.sort(key=len)
animals
for length, group in itertools.groupby(animals, len): #
    print(length, '->', list(group))

for length, group in itertools.groupby(reversed(animals), len): #
    print(length, '->', list(group))

# itertools.tee yields multiple generators, each yielding every item of
# the input generator.

list(itertools.tee('ABC'))

g1, g2 = itertools.tee('ABC')
next(g1)
next(g2)
next(g2)
list(g1)
list(g2)
list(zip(*itertools.tee('ABC')))



import itertools

# Filtering generator function in standard library

def vowel(c):
    return c.lower() in 'aeiou'

list(filter(vowel, 'Aardvark'))

list(itertools.filterfalse(vowel, 'Aardvark'))

list(itertools.dropwhile(vowel, 'Aardvark'))

list(itertools.takewhile(vowel, 'Aardvark'))

list(itertools.compress('Aardvark', (1,0,1,1,0,1)))

list(itertools.islice('Aardvark', 4))

list(itertools.islice('Aardvark', 4, 7))

list(itertools.islice('Aardvark', 1, 7, 2))
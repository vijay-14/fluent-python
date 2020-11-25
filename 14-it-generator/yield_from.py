def chain(*iterables):
    for it in iterables:
        for i in it:
            yield i
s = 'ABC'
t = tuple(range(3))
list(chain(s, t))

def chain1(*iterables):
    for i in iterables:
        yield from i
list(chain1(s, t))

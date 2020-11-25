def factorial(m):
    '''returns n!'''
    return 1 if m < 2 else m * factorial(m-1)

factorial.__doc__
factorial(42)

fact = factorial
fact
fact(5)
map(factorial, range(11))
list(map(fact, range(11)))


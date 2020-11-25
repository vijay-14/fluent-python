class X():
    x1 = 'x'
    __slots__ = ('__a')

    def __init__(self, a):
        self.__a = a
x1 = X(1)
dir(x1)
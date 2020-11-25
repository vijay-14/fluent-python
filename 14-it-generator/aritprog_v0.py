from fractions import Fraction
from decimal import Decimal

class ArithmeticProgression:

    def __init__(self, begin, step, end=None):
        self.begin = begin
        self.step = step
        self.end = end  # May run forever

    def __iter__(self):
        result = type(self.begin + self.step)(self.begin)
        forever = self.end is None
        index = 0
        while forever or result < self.end:
            yield result
            index += 1
            result = self.begin + self.step * index

ap_int = ArithmeticProgression(0,1,100)
ap_frac = ArithmeticProgression(0, Fraction(1,4))
ap_decm = ArithmeticProgression(100, Decimal('0.5'))
def print_ap(ap):
    endif_p = 5
    for p in ap:
        if endif_p != 0:
            print(p)
            endif_p -= 1
        else:
            break

print_ap(ap_int)
print_ap(ap_frac)
print_ap(ap_decm)
# begin = 0
# step = Fraction(1,3)

# print(type(type(begin + step)(begin)))

import itertools
from fractions import Fraction
from decimal import Decimal

def aritprog_gen(begin, step, end=None):
    first = type(begin+step)(begin)
    ap_gen = itertools.count(first,step)
    if end is not None:
        ap_gen = itertools.takewhile(lambda n: n < end, ap_gen)
    return ap_gen

ap_int = aritprog_gen(0,1,100)
ap_frac = aritprog_gen(0, Fraction(1,4))
ap_decm = aritprog_gen(100, Decimal('0.5'))
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



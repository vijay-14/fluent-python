with open('mirror.py') as fp: 
    src = fp.read(60)

print(len(src))
print(fp, fp.closed, fp.encoding)

# from mirror import LookingGlass
# BEGIN MIRROR_EX
class LookingGlass:

    def __enter__(self):  # <1>
        import sys
        self.original_write = sys.stdout.write  # <2>
        sys.stdout.write = self.reverse_write  # <3>
        return 'JABBERWOCKY'  # <4>

    def reverse_write(self, text):  # <5>
        self.original_write(text[::-1])

    def __exit__(self, exc_type, exc_value, traceback):  # <6>
        import sys  # <7>
        sys.stdout.write = self.original_write  # <8>
        if exc_type is ZeroDivisionError:  # <9>
            print('Please DO NOT divide by zero!')
            return True  # <10>
        # <11>


# END MIRROR_EX
with LookingGlass() as what:
    print('Alice, Kitty and Snowdrop')
    print(what)
print(what)
print('Back to normal.')

# Exercising LookingGlass without a with block.
import sys
manager = LookingGlass()
manager
monster = manager.__enter__()
monster == 'JABBERWOCKY'
manager
manager.__exit__(None,None,None)

import contextlib


@contextlib.contextmanager
def looking_glass():
    import sys
    original_write = sys.stdout.write
    def reverse_write(text):
        original_write(text[::-1])
    sys.stdout.write = reverse_write
    yield 'JABBERWOCKY'
    sys.stdout.write = original_write

manager = looking_glass()
manager
monster = manager.__enter__()
monster == 'JABBERWOCKY'
manager
manager.__exit__(None,None,None)

with looking_glass() as what:
    print('Alice, Kitty and Snowdrop')
    print(what)
print(what)
print('Back to normal.')

#  A context manager for rewriting files in place.
import csv
with inplace(csvfilename, 'r', newline='') as (infh, outfh):
    reader = csv.reader(infh)
    writer = csv.writer(outfh)
for row in reader:
    row += ['new', 'columns']
    writer.writerow(row)







import re
import reprlib
from collections import abc

RE_WORD = re.compile(r'\w+')

class Sentence:

    def __init__(self, text):
        self.text = text
    
    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        return (match.group() for match in RE_WORD.finditer(self.text))

text = '"Thats a Beautiful Sky! Try to reach it."'
t = Sentence(text)
print(t)
for w in t:
    print(w)

print(issubclass(Sentence, abc.Iterable))

print(isinstance(t, abc.Iterable))
import re
import reprlib
from collections import abc

RE_WORD = re.compile(r'\w+')

class Sentence:

    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return 'Sentece(%s)' % reprlib.repr(text)

    def __iter__(self):
        for match in RE_WORD.finditer(self.text):
            yield match.group()

text = '"Thats a Beautiful Sky! Try to reach it."'
t = Sentence(text)
print(t)
for w in t:
    print(w)

print(issubclass(Sentence, abc.Iterable))

print(isinstance(t, abc.Iterable))
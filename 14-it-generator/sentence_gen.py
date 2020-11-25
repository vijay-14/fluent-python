import re
import reprlib
from collections import abc

RE_WORD = re.compile(r'\w+')

class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)
    
    def __iter__(self):
        for word in self.words:
            yield word
        return

text = '"Thats a Beautiful Sky! Try to reach it."'
t = Sentence(text)
print(t)
for w in t:
    print(w)

print(issubclass(Sentence, abc.Iterable))

print(isinstance(t, abc.Iterable))



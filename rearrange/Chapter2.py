# Slicing
s = 'bicycle'
s[::-1] # reversed list
# Arrays
from array import array
from random import random
floats = array('d', (random() for i in range(10**7)))
floats[-1]
fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()
floats2 = array('d')
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10**7)
fp.close()
floats2[-1]
floats2 == floats
# Numpy and Scipy
import numpy as np
a = np.arange(12)
a
type(a)
a.shape = 3,4
a[:,1]
a.transpose()
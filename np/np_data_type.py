import numpy as np

## numpy data types

adt = np.array([1, 2, 3, 4])
print(adt.dtype)

adts = np.array(['apple', 'banana', 'cherry'])
print(adts.dtype)

asr = np.array([1, 2, 3, 4], dtype='S')
print(asr)
print(asr.dtype)

air = np.array([1, 2, 3, 4], dtype='i4')
print(air)
print(air.dtype)

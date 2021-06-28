import numpy as np

## array slicing
ars = np.array([1, 2, 3, 4, 5, 6, 7])
print(ars[1:5])
print(ars[4:])
print(ars[:4])
print(ars[-5:-1])
print(ars[1:5:2])
print(ars[::2])
print(ars[::3])

ard = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(ard[1, 1:4])
print(ard[0:2, 2])
print(ard[0:2, 1:4])

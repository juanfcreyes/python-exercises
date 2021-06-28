import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

print('arr iterarion one level:')
for x in arr:
  print(x)

print('\narr iterarion two levels:')
for x in arr:
  for y in x:
    print(y)


print('\na3d iterarion one level 3d array:')
a3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in a3d:
  print(x)

print('\narr iterarion with nditer:')
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr):
  print(x)


print('\nari iterarion with diferrent data types:')
ari = np.array([1, 2, 3])
for x in np.nditer(ari, flags=['buffered'], op_dtypes=['S']):
  print(x)


print('\nars iterarion with diferrent step size:')
ars = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np.nditer(ars[:, ::2]):
  print(x)

print('\nare iterarion with enumeratios:')
are = np.array([1, 2, 3])
for idx, x in np.ndenumerate(are):
  print(idx, x)


print('\nare iterarion with enumeratios 2d:')
a2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for idx, x in np.ndenumerate(a2d):
  print(idx, x)

import numpy as np

## shape 
arr = np.array([[1, 2, 3, 4, 5], [5, 6, 7, 8]])
print('arr:', arr)
print('arr shape:', arr.shape)

ad5 = np.array([1, 2, 3, 4], ndmin=5)
print('ad5 :', ad5)
print('shape of array:', ad5.shape)

## reshape arrays
ars = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = ars.reshape(4, 3)
print('newarr:')
print(newarr)


ad3 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
nard3 = ad3.reshape(2, 3, 2)
print('nard3:')
print(nard3)
print('nard3 base:', nard3.base)

arc = np.array([1, 2, 3, 4, 5, 6, 7, 8])
calc = arc.reshape(2, 2, -1)
print('arc:', arc)
print('calc')
print(calc)

## flattening the arrays
arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print('arr:')
print(arr)
print('newarr:',newarr)


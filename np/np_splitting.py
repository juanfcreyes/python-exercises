import numpy as np

## Splitting munpy arrays
arr = np.array([1, 2, 3, 4, 5, 6])
print('original array:', arr)
newarr = np.array_split(arr, 3)
print('split array in 3 parts:', newarr)
newarr = np.array_split(arr, 4)
print('split array in 3 parts:', newarr)

## Split the 2-D
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
print('\noriginal 2-d array:')
print(arr)
newarr = np.array_split(arr, 3)
print('split 2-d array in 3 parts')
print(newarr)

## Split the 2-D along rows
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
print('\noriginal 2-d array:')
print(arr)
newarr = np.array_split(arr, 3, axis=1)
print('split 2-d array in 3 parts along rows')
print(newarr)

## Split the 2-D along rows with hsplit
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
print('\noriginal 2-d array:')
newarr = np.hsplit(arr, 3)
print('split 2-d array in 3 parts along rows hsplit')
print(newarr)

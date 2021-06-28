import numpy as np

## simple sort
arr = np.array([3, 2, 0, 1])
print('Original array', arr)
print('Sorted array:', np.sort(arr))

## simple sort strings
arr = np.array(['banana', 'cherry', 'apple'])
print('\nOriginal array strings', arr)
print('Sorted array strings:', np.sort(arr))

## simple sort booleans
arr = np.array([True, False, True])
print('\nOriginal array booleans', arr)
print('Sorted array booleans:', np.sort(arr))

## sorting 2-d array
arr = np.array([[3, 2, 4], [5, 0, 1]])
print('\nOriginal array 2-d')
print(arr)
print('Sorted array 2-d:')
print(np.sort(arr))

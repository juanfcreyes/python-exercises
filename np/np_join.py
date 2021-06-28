import numpy as np

## concatenation
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print('array join')
print('array arr1:', arr1)
print('array arr2:', arr2)
print('array arr contatenated:', arr)

## concatenation by axis
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)
print('\narray join by axis')
print('array arr1:')
print(arr1)
print('array arr2:')
print(arr2)
print('array arr contatenated axis:')
print(arr)

## concatenation with stack
print('\narray join with stack')
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2))
print('array arr1:', arr1)
print('array arr2:', arr2)
print('array arr contatenated with stack:')
print(arr)

## concatenation with stack by axis
print('\narray join with stack')
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2), axis=1)
print('array arr1:', arr1)
print('array arr2:', arr2)
print('array arr contatenated with stack by axis:')
print(arr)

## hstack() to stack along rows
print('\narray join with hstack')
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.hstack((arr1, arr2))
print('array arr1:', arr1)
print('array arr2:', arr2)
print('array arr joined with hstack:')
print(arr)


## vstack() to stack along columns
print('\narray join with vstack')
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.vstack((arr1, arr2))
print('array arr1:', arr1)
print('array arr2:', arr2)
print('array arr joined with vstack:')
print(arr)


## dstack() to stack along columns
print('\narray join with vstack')
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.dstack((arr1, arr2))
print('array arr1:', arr1)
print('array arr2:', arr2)
print('array arr joined with dstack:')
print(arr)

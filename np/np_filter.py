import numpy as np

## FIlter with hard-coded
arr = np.array([41, 42, 43, 44])
filter_arr = [True, False, True, False]
newarr = arr[filter_arr]
print('Origin array:', arr)
print('Filter array:', filter_arr)
print('Array filtered:', newarr)

## filter directly from array
arr = np.array([41, 42, 43, 44])
filter_arr = arr > 42
newarr = arr[filter_arr]
print('\nOrigin array:', arr)
print('Filter array:', filter_arr)
print('Array filtered:', newarr)


arr = np.array([1, 2, 3, 4, 5, 6, 7])
filter_arr = arr % 2 == 0
newarr = arr[filter_arr]
print('\nOrigin array:', arr)
print('Filter array:', filter_arr)
print('Array filtered:', newarr)

## filter with np where
arr = np.array([41, 42, 43, 44])
filter_arr = np.where(arr > 42)
newarr = arr[filter_arr]
print('\nOrigin array:', arr)
print('Filter array:', filter_arr)
print('Array filtered:', newarr)

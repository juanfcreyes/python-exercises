import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))

## arrays dimensions
a0D = np.array(50)
a1D = np.array([1, 2, 3, 4, 5])
a2D = np.array([[1, 2, 3], [4, 5, 6]])
a3D = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print('a0D', a0D, a0D.ndim)
print('a1D', a1D, a1D.ndim)
print('a2D', a2D, a2D.ndim)
print('a3D', a3D, a3D.ndim)

a5D = np.array([1, 2, 3, 4], ndmin=5)

print(a5D)
print('number of dimensions :', a5D.ndim)


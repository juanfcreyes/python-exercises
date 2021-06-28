import numpy as np

print('np version:', np.__version__)

arr = np.arange(10)
print('np 0-9 array:', arr)

print('np 3x3 2-d booleans:')
print(np.full((3,3), True ,dtype=bool))

copy = np.copy(arr)

print('odd numbers fom [0-9]: ', copy)

copy[copy % 2 != 0] = -1
print('replce odd numbers fom [0-9] fo -1: ', copy)

new_copy = np.where(arr % 2 != 0, -1, arr)
print('replce odd numbers fom [0-9] fo -1: ', new_copy)

print('reshape arr:')
print(np.reshape(arr, (2,-1)))


a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)
print('Stack arrays a and b vertically')
print(np.vstack((a, b)))

a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)
print('Stack arrays a and b horizontally')
print(np.hstack((a, b)))

a = np.array([1,2,3]) 
print('Create pattern')
print(np.concatenate((np.repeat(a, 3), np.tile(a, 3))))


a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])
print('Create filter')
print(np.setdiff1d(a, b))


a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
print('Index of same element')
print(np.where(a == b))

a = np.array([2, 6, 1, 9, 10, 3, 27])
print('all items between 5 and 10 from a')
print(a[(a >= 5) & (a <= 10)])







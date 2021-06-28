import numpy as np

## arrays indexing
ai = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st dim: ', ai[0, 1])
print('5th element on 2nd dim: ', ai[1, 4])

ai3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(ai3d[0, 1, 2])

ani = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('Last element from 2nd dim: ', ani[1, -1])

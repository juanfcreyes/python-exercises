import numpy as np

def maxx(x, y):
    """Get the maximum of two items"""
    if x >= y:
        return x
    else:
        return y

pair_max = np.vectorize(maxx, otypes=[float])


a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])
print(np.where(a >= b, a, b))
print(pair_max(a, b))


arr = np.arange(9).reshape(3,3)
print('swap colum 0 and 1')
print(arr[:, [1,0,2]])
print('swap colum 1 and 2')
print(arr[:, [0,2,1]])
print('swap colum 0 and 2')
print(arr[:, [2,1,0]])


print('swap row 2-d array (reverse)')
print('method 1 arr[[2, 1, 0],:]')
print(arr[[2, 1, 0],:])
print('method 2 arr[::-1]')
print(arr[::-1])

print('2D array of shape 5×3 that contain random decimal numbers between 5 and 10')
print('method 1 (5 * np.random.random_sample((5, 3))) + 5')
limited_values = (5 * np.random.random_sample((5, 3))) + 5
print(limited_values)
print(limited_values[:, 2])
print('method 2 np.random.uniform(5,10, size=(5,3))')
print(np.random.uniform(5,10, size=(5,3)))
print('method 3 np.random.randint(low=5, high=10, size=(5,3)) + np.random.random((5,3))')
print(np.random.randint(low=5, high=10, size=(5,3)) + np.random.random((5,3)))


rand_arr = np.random.random((5,3))
np.set_printoptions(precision=3)
print(rand_arr)

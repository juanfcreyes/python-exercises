from numpy import random
import numpy as np


## ramdom numbers
x = random.randint(100)
print('random integer number under 100: ', x)

x = random.rand()
print('\nrandom number between 0 and 1:', x)

x=random.randint(100, size=(5))
print('\nrandom  integer number array of five elements:', x)

x = random.randint(100, size=(3, 5))
print('\n2-D array with 3 rows, each row containing 5 random numbers:')
print(x)

x = random.rand(5)
print('\n1-D array containing 5 random floats')
print(x)

x = random.rand(3, 5)
print('\n2-D array with 3 rows, each row containing 5 random numbers:')
print(x)


## data distribution
x = random.choice([3, 5, 7, 9], p=[0.4, 0.3, 0.2, 0.1], size=(100))
print('data distribution base on probabilities in an array of one hundred elements:', x)
print(len(x[x == 3 ]) / 100)
print(len(x[x == 5 ]) / 100)
print(len(x[x == 7 ]) / 100)
print(len(x[x == 9 ]) / 100)

print('data distribution base on probabilities that return an 2-D array with 3 rows, each containging 5 values.')
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))
print(x)

## random permutations
arr = np.array([1, 2, 3, 4, 5])
random.shuffle(arr)
print('suffle the array order:', np.array([1, 2, 3, 4, 5]), arr)

arr = np.array([1, 2, 3, 4, 5])
print('get a random permutation of arr:', arr, random.permutation(arr))

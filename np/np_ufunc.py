import numpy as np

x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = []
print(zip(x, y))
for i, j in zip(x, y):
  z.append(i + j)
print('add between two arrays without ufunc', z)

z = np.add(x, y)
print('add between two arrays without ufunc', z)

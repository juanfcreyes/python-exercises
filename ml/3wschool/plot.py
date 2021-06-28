import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

"""
Data Distribution
We use the array from the example above to draw a histogram with 5 bars.
The first bar represents how many values in the array are between 0 and 1.
The second bar represents how many values are between 1 and 2.
Etc.

Which gives us this result:
52 values are between 0 and 1
48 values are between 1 and 2
49 values are between 2 and 3
51 values are between 3 and 4
50 values are between 4 and 5
"""
x = np.random.uniform(0.0, 5.0, 250)
plt.hist(x,5)
plt.show()

x = np.random.uniform(0.0, 5.0, 100000)
plt.hist(x, 100)
plt.show()


"""
Normal Data Distribution
"""
x = np.random.normal(5.0, 1.0, 100000)
plt.hist(x, 100)
plt.show()

"""
Scatter Plot
"""

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

plt.scatter(x, y)
plt.show()


x = np.random.normal(5.0, 1.0, 1000)
y = np.random.normal(10.0, 2.0, 1000)

plt.scatter(x, y)
plt.show()

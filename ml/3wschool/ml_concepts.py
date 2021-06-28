import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

"""
In Machine Learning (and in mathematics)
there are often three values that interests us:

Mean - The average value
Median - The mid point value
Mode - The most common value
"""

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
print('data set', speed)

x = np.mean(speed)
print('mean', x)

x = np.median(speed)
print('median', x)

x = stats.mode(speed)
print('mode', x, "\n")


"""
Variance is another number that indicates how spread out the values are.

In fact, if you take the square root of the variance, you get the standard deviation!

Or the other way around, if you multiply the standard deviation by itself, you get the variance!

To calculate the variance you have to do as follows:

1. Find the mean:
    (32+111+138+28+59+77+97) / 7 = 77.4
    
2. For each value: find the difference from the mean:

     32 - 77.4 = -45.4
    111 - 77.4 =  33.6
    138 - 77.4 =  60.6
    .
    .
    .
    

3. For each difference: find the square value:

    (-45.4)2 = 2061.16
    (33.6)2 = 1128.96
    (60.6)2 = 3672.36
    .
    .
    .

4. The variance is the average number of these squared differences:
    (2061.16+1128.96+3672.36+2440.36+338.56+0.16+384.16) / 7 = 1432.2
"""
speed = [32,111,138,28,59,77,97]
print('data set', speed)

x = np.var(speed)
print('variance', x, "\n")


"""
As we have learned,
the formula to find the standard deviation is the square root of the variance:
"""
speed = [32,111,138,28,59,77,97]
print('data set', speed)

x = np.std(speed)
print('standar deviation', x, "\n")

"""
Standard deviation is a number that describes
how spread out the values are.

A low standard deviation means that most of the numbers
are close to the mean (average) value.

A high standard deviation means that the values are
spread out over a wider range.
"""
speed = [86,87,88,86,87,85,86]
print('data set', speed)

x = np.std(speed)
print('low standar deviation', x)

speed = [32,111,138,28,59,77,97]
print('data set', speed)

x = np.std(speed)
print('high standar deviation', x)



"""
Percentiles are used in statistics to give you a number that describes
the value that a given percent of the values are lower than.
"""

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
print('data set', ages)

x = np.percentile(ages, 75)
print('percentile', x)

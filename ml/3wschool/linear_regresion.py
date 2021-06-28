import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

"""
Linear Regresion
"""
def generate_model(x, y):
    slope, intercept, r, p, std_err = stats.linregress(x, y)
    model_func = lambda x : slope * x + intercept
    mymodel = list(map(model_func, x))
    return model_func, mymodel, r;


x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

model_func, mymodel, r = generate_model(x, y)
print('mymodel', mymodel)
print('r-squared', r)

"""
predict value
"""
speed = model_func(10)

plt.scatter(x, y)
plt.scatter(10, speed, color='red')
plt.plot(x, mymodel)
plt.show()



"""
Bad Fit
Example where linear regression is not valid
"""
x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

model_func, mymodel, r = generate_model(x, y)
print('mymodel', mymodel)
print('r-squared', r)

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()


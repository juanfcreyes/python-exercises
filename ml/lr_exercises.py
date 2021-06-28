import numpy as np
import pandas as pd
import sklearn 
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

x = np.array([0, 1, 2, 3, 4]).reshape(-1, 1)
y = np.array([2, 3, 5, 4, 6])

model = LinearRegression()
model.fit(x, y)

y_predicted = model.predict(x)

# model evaluation
rmse = mean_squared_error(y, y_predicted)
r2 = r2_score(y, y_predicted)

# printing values
print('Slope:' ,model.coef_)
print('Intercept:', model.intercept_)
print('Root mean squared error: ', rmse)
print('R2 score: ', r2)

forecast = model.predict([[10]])
arr_x = np.concatenate((x, np.array([[10]])), axis=0)
arr_y = np.concatenate((y_predicted, forecast))

#plt.scatter(x, y, s=10)
#plt.scatter(10, forecast, s=10)
#plt.plot(arr_x, arr_y , color='r')
#plt.xlabel('x')
#plt.ylabel('y')
#plt.show()

# other example
np.random.seed(0)
n = 20   
x = np.linspace(0, 10, n)
r_x = x.reshape(-1, 1)
y = 1 + (x * 2) + (1 * np.random.randn(n)) 
model = LinearRegression(fit_intercept=True)
model.fit(r_x, y)

xfit = np.linspace(0,10,100).reshape(-1, 1)
yfit = model.predict(xfit)
y_predicted = model.predict(r_x)

# model evaluation
rmse = mean_squared_error(y, y_predicted)
r2 = r2_score(y, y_predicted)

# printing values
print('-------------------')
print('Slope:' ,model.coef_)
print('Intercept:', model.intercept_)
print('Root mean squared error: ', rmse)
print('R2 score: ', r2)

#plt.plot(xfit, yfit, color="black")
#plt.plot(np.vstack([x, x]), np.vstack([y, model.predict(r_x)]),color="red");
#plt.scatter(x, y)
#plt.show()


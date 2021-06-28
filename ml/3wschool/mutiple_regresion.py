from sklearn.metrics import r2_score
from sklearn import linear_model
import numpy as np
import pandas
import matplotlib.pyplot as plt

df = pandas.read_csv("cars.csv")

x = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(x, y)

"""
predict the CO2 emission of a car where the weight is 2300kg,
and the volume is 1300ccm:
"""
print("coefficents regression", regr.coef_)
print("coefficents intercept", regr.intercept_)

predictedCO2 = regr.predict([[2300, 1300]])
print("predicted value", predictedCO2)

predictedCO2 = regr.predict([[3300, 1300]])
print("predicted value II", predictedCO2)

plt.figure(figsize=(8, 4))
plt.subplots_adjust(wspace = 0.5, hspace = 1)

plt.subplot(1,2,1)
plt.title('Weight vs CO2')
plt.scatter(df['Weight'], df['CO2'])
plt.xlabel('Weigth')
plt.ylabel('CO2')

plt.subplot(1,2,2)
plt.title('Volume vs CO2')
plt.scatter(df['Volume'], df['CO2'])
plt.xlabel('Volume')
plt.ylabel('CO2')

plt.show()


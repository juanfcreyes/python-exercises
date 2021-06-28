from sklearn.metrics import r2_score
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()
import numpy as np
import pandas
import matplotlib.pyplot as plt

df = pandas.read_csv("cars.csv")
df['Volume'] = df['Volume'] / 1000;

X = df[['Weight', 'Volume']]
y = df['CO2']

scaledX = scale.fit_transform(X)

regr = linear_model.LinearRegression()
regr.fit(scaledX, y)

print("coefficents regression", regr.coef_)
print("coefficents intercept", regr.intercept_)

scaled = scale.transform([[2300, 1.3]])
predictedCO2 = regr.predict([scaled[0]])
print("predicted value", predictedCO2)

scaled = scale.transform([[3300, 1.3]])
predictedCO2 = regr.predict([scaled[0]])
print("predicted value II", predictedCO2)

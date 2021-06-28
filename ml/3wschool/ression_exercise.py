from sklearn.metrics import r2_score
from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas
import matplotlib.pyplot as plt

df = pandas.read_csv("cardio_train.csv", delimiter=";")
print(df)
x = np.array(df[['cholesterol', 'active', 'gender', 'alco', 'smoke']]).reshape(-1, 5)
y = np.array(df['cardio'])

model = LogisticRegression()
model.fit(x, y)

print('clases',model.classes_)
print('score', model.score(x, y))
print('intercept', model.intercept_)
print('coef', model.coef_)

test_array = [[3, 0, 2, 0  ,0], [2, 1, 1, 0, 0 ], [1, 1, 1, 1, 1]]
print(model.predict_proba(test_array))
print(model.predict(test_array))

import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
np.random.seed(2)

x = np.random.normal(3, 1, 100)
y = np.random.normal(150, 40, 100) / x


train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

mymodel = np.poly1d(np.polyfit(train_x, train_y, 4))

"""
R2
Remember R2, also known as R-squared?

It measures the relationship between the x axis and the y axis,
and the value ranges from 0 to 1,
where 0 means no relationship, and 1 means totally related.

The sklearn module has a method called r2_score()
that will help us find this relationship.

In this case we would like to measure the
relationship between the minutes a customer
stays in the shop and how much money they spend.
"""
r2 = r2_score(train_y, mymodel(train_x))
print(r2)

r2 = r2_score(test_y, mymodel(test_x))
print(r2)

print(mymodel(5))

myline = np.linspace(0, 6, 100)
plt.scatter(5, mymodel(5), color='red')
plt.scatter(5.4, mymodel(5.4), color='red')
plt.scatter(train_x, train_y)
plt.plot(myline, mymodel(myline))
plt.show()

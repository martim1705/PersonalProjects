import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

df = pd.read_csv("https://content.codecademy.com/programs/data-science-path/linear_regression/honeyproduction.csv")

prod_per_year = df.groupby('year').mean().reset_index()

X = prod_per_year['year']
X = X.values.reshape(-1,1)

y = prod_per_year['totalprod']

plt.scatter(X, y)
plt.show()

regr = linear_model.LinearRegression()
regr.fit(X,y)
print(regr.coef_)
print(regr.intercept_)

y_predict = regr.predict(X)

plt.scatter(X, y)
plt.plot(X, y_predict, color='red')
plt.show()

X_future = np.array(range(2013,2051))
X_future = X_future.reshape(-1,1)

future_predict = regr.predict(X_future)

plt.plot(X_future, future_predict)
plt.show()
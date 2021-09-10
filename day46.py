import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('bluegills.csv')
feat = dataset.iloc[:, 0:1].values
lab = dataset.iloc[:, 1].values

#fitting linear regression -->
from sklearn.linear_model import LinearRegression
linObj = LinearRegression()
linObj.fit(feat, lab)
#plot a graph for feat and lab for visualisation -->
featGrid = np.arange(min(feat), max(feat), 0.1)
featGrid = featGrid.reshape(len(featGrid), 1)
plt.scatter(feat, lab, color = 'yellow')
plt.plot(featGrid, linObj.predict(featGrid), color = 'blue')
plt.title('Bluegill (Linear Regression)')
plt.xlabel('Age')
plt.ylabel('Length')
plt.show()

#fitting polynomial regression  -->
from sklearn.preprocessing import PolynomialFeatures
higherDegree = PolynomialFeatures(degree = 2)
featPoly = higherDegree.fit_transform(feat)
regressorPoly = LinearRegression()
regressorPoly.fit(featPoly, lab)

# scatter and plot graph for the polynomial conversion of feat -->
featGrid = np.arange(min(feat), max(feat), 0.1)
featGrid = featGrid.reshape(len(featGrid), 1)
plt.scatter(feat, lab, color = 'yellow')
plt.plot(featGrid, regressorPoly.predict(higherDegree.fit_transform(featGrid)), color = 'blue')
plt.title('Bluegill (Linear Regression)')
plt.xlabel('Age')
plt.ylabel('Length')
plt.show()

print ("prediction using linear regression :"+str(linObj.predict([[5]])))
print ("predicting using polynomial regression :"+str(regressorPoly.predict(higherDegree.fit_transform([[5]]))))



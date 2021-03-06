import pandas as pd

studentData=pd.read_csv("student_scores.csv")

studentData.shape
studentData.columns.tolist()

studentData.isnull().any(axis=0)

features=studentData['Hours'].values

labels=studentData['Scores'].values

import matplotlib.pyplot as plt
plt.scatter(features,labels)

from sklearn.linear_model import LinearRegression

#create object
regressor=LinearRegression()

#model
features=features.reshape(25,1)

regressor.fit(features,labels)

m=regressor.coef_

c=regressor.intercept_

x=9
y=(m*x)+c

regressor.predict([[9]])

regressor.predict(features)

plt.scatter(features,labels)
plt.plot(features,regressor.predict(features))
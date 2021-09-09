import numpy as np
import pandas as pd

# read the dataset
dataset = pd.read_csv('Female_Stats.csv')
print(dataset.dtypes)

# differentiate feat and lab
feat = dataset.iloc[:,1:].values
lab = dataset.iloc[:, [0]].values

#check for any missing data or nan -->
dataset.isnull().any(axis=0)

from sklearn.model_selection import train_test_split
featTrain, featTest, labTrain, labTest = train_test_split(feat, lab, test_size = 0.2, random_state = 0)

#fiting multiple linear regression -->
from sklearn.linear_model import LinearRegression
obj = LinearRegression()
obj.fit(featTrain, labTrain)

pred = obj.predict(featTest)

print (pd.DataFrame(zip(np.round(pred,2), labTest)))

import statsmodels.api as sm

featsm = sm.add_constant(feat)
estimate1 = sm.OLS(lab, featsm)
estimate2 = estimate1.fit()

print (estimate2.summary())

print (obj.coef_[0][1])

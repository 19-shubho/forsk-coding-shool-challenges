import pandas as pd
#read the csv file -->
dataset = pd.read_csv('IQ_Size.csv')
feat = dataset.iloc[:, 1:].values
lab = dataset.iloc[:, 0].values
#split the data set in to two parts: train and testimate -->
from sklearn.model_selection import train_test_split
featTrain, featTestimate, labTrain, labTestimate = train_test_split(feat, lab, test_size = 0.2, random_state = 0)

#fitting multiple linear regression
from sklearn.linear_model import LinearRegression
obj = LinearRegression()
obj.fit(featTrain, labTrain)

# task01 --> prediction for brain size 90, heigth 70, weight 150
obj.predict([[90,70,150]])
# BACKWARD ELEMINATION PROCESS BEGINS
import statsmodels.api as sm
feat = sm.add_constant(feat)
featsm = feat[:,[0,1,2,3]]
estimate = sm.OLS(lab, featsm)
estimate = estimate.fit()
print (estimate.summary())

#del weight colomn
featsm = feat[:, [0, 1, 2]]
estimate = sm.OLS(lab, featsm)
estimate = estimate.fit()
print (estimate.summary())

#remove constant
featsm = feat[:, [1, 2]]
estimate = sm.OLS(lab, featsm)
estimate = estimate.fit()
print (estimate.summary())

#remove height
featsm = feat[:, [1]]
estimate = sm.OLS(lab, featsm)
estimate = estimate.fit()
print (estimate.summary())

print ("ONLY BRAIN SIZE IS USEFUL WHILE PREDICTING INTELLIGENCE.")




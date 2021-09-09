import pandas as pd
#read csv file
salData = pd.read_csv("Salary_Classification.csv")

salData.shape

salData.columns

salData.dtypes
#Check if any empty spaces 
salData.isnull().any(axis = 0)

#take out feat and lab using iloc
feat = salData.iloc[:,0:4].values
lab = salData.iloc[:,-1].values

#department columns
#we need to convert categorical data to numeric representation
#encode our categorical data in numeric
#onehotencoding

#info -> encoded (Morse code) -> transmission -> decode -> info

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

colTransform = ColumnTransformer([('encoder', OneHotEncoder(), [0])], remainder ='passthrough' )

import numpy as np
feat = np.array(colTransform.fit_transform(feat), dtype = np.float32)

feat = feat[:,1:]

#train test split
from sklearn.model_selection import train_test_split


featTrain, featTrain, labTrain, labTrain = train_test_split(feat, lab, test_size = 0.2)


#feature scaling

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()

featTrain = sc.fit_transform(featTrain)
#80%
#fit -> mean, std
#transform -> formula


featTrain = sc.transform(featTrain)
#20%
#fit_transform, fit - mean, std
#transform _ mean, std from tain data




from sklearn.linear_model import LinearRegression

#create object
obj = LinearRegression()

#model


obj.fit(featTrain, labTrain)


pred = obj.predict(featTrain)



pd.DataFrame(zip(pred, labTrain))


predTrain = obj.predict(featTrain)



pd.DataFrame(zip(predTrain, labTrain))

#score
#train score
obj.score(featTrain, labTrain)
#predict(featTrain)
#compare with labTrain

#test score


obj.score(featTrain, labTrain)


#development, 1100, 2, 3 -> salary




x = ['Development',1100, 2, 3]

x = np.array(x)

x = x.reshape(1,4)

x = np.array(colTransform.transform(x), dtype = np.float32)


x = x[:,1:]
#transform

obj.predict(x)





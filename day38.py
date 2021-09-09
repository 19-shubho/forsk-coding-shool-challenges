import pandas as pd

dataset = pd.read_csv("Salary_Classification.csv")

dataset.shape

dataset.columns

dataset.dtypes

dataset.isnull().any(axis = 0)

#features and labels
#0,1,2,3 
features = dataset.iloc[:,0:4].values
labels = dataset.iloc[:,-1].values

#department columns
#we need to convert categorical data to numeric representation
#encode our categorical data in numeric
#onehotencoding

#info -> encoded (Morse code) -> transmission -> decode -> info

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

cTransformer = ColumnTransformer([('encoder', OneHotEncoder(), [0])], remainder ='passthrough' )

import numpy as np
features = np.array(cTransformer.fit_transform(features), dtype = np.float32)

#train test split
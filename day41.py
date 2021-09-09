import pandas as pd
import numpy as np
#read the dataset
dataset = pd.read_csv('Salary_Classification.csv')
dataset.shape
dataset.columns
dataset.dtypes
dataset.isnull().any(axis = 0)
#differentiate features and labels
feat = dataset.iloc[:,0:4].values
lab = dataset.iloc[:,-1].values

#convert category wise data into numeric info
#use onehotencoding
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

cTransf = ColumnTransformer([('encoder', OneHotEncoder(), [0])], remainder ='passthrough' )
feat = np.array(cTransf.fit_transform(feat), dtype = np.float32)
feat = feat[:,1:]

#BACKWARD ELEMINATION PROCESS
import statsmodels.api as sm
import numpy as np

#improvising the constant coloumn
feat = sm.add_constant(feat)

#calculate p value using a while loop 
#until it is left with only one required feature(automation)

featOptimal = feat[:, [0,1,2,3,4,5]]

while (True):
    objOLS = sm.OLS(endog = lab,exog =featOptimal).fit()
    P = objOLS.pvalues
    if P.max() > 0.05 :
        featOptimal = np.delete(featOptimal, P.argmax(),1)
    else:
        break
    
print (featOptimal.shape)
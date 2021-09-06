import pandas as pd

#read the foodTruck cscv file for further operations -->
DATA = pd.read_csv("Foodtruck.csv")

popl = DATA.iloc[:,0:1].values
prof = DATA.iloc[:,1:2].values

#break the data into two for taining and testing -->
from sklearn.model_selection import train_test_split
poplTrain, poplTest, profTrain, profTest = train_test_split(popl, prof, test_size = 0.2, random_state = 0)

#import linear regression class -->
from sklearn.linear_model import LinearRegression
#make object of the class
object = LinearRegression()

#fitting the model -->
object.fit(poplTrain, profTrain)

#find the prediction on jaipur city
object.predict([[3.073]])

#find prediction for any higher population city
object.predict([[33.4]])

'''
def pred(x):
    p=object.predict([[x]])
    if (p > 0):
        print('profit made is: '+str(p))
    else :
        print('loss incurred is: '+str(p))
'''  
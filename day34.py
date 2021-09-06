import pandas as pd

#read the cars csv file using numpy -->
carData=pd.read_csv('cars.csv')





#x1st method -->

#train test split is performed -->
from sklearn.model_selection import train_test_split

carDataTrain, carDataTest=train_test_split(carData, test_size=0.5, random_state=0)
carDataTrain.to_csv('carDataTrain.csv', index=False)
carDataTest.to_csv("carDataTest.csv", index=False)





#2nd method -->

#get the value of features in a new dataFrame altogather
feat=carData.iloc[:,1:].values
#get the value of labels in a new dataFrame altogather....price is set to labels
lab=carData.iloc[:,0].values

#get your coloumns in a clean list format
print(carData.columns.tolist())

#now split the new carData into training and testing 
from sklearn.model_selection import train_test_split
featTrain, featTest, labTrain, labTest=train_test_split(feat, lab, test_size=0.5, random_state=0)
import pandas as pd

studentData=pd.read_csv("student_scores.csv")

studentData.shape
studentData.columns.tolist()
#to check if any coloumn is missing some data-->
studentData.isnull().any(axis=0)

features=studentData['Hours'].values

labels=studentData['Scores'].values

#testing and training of model begins divide your features and labels data
# into required proportions so that you can easily train and test your model.
from sklearn.model_selection import train_test_split
featTrain, featTest, labTrain, labTest=train_test_split(features, labels, test_size=0.2)

#import LinearRegression class from sklearn module
from sklearn.linear_model import LinearRegression

#create object
regressor=LinearRegression()

#model
#features=features.reshape(25,1)
featTrain=featTrain.reshape(20,1)

#regressor.fit(features,labels)
regressor.fit(featTrain, labTrain)

featTest=featTest.reshape(5,1)

#regressor.predict(features)
predict=regressor.predict(featTest)

pd.DataFrame(zip(predict, labTest))


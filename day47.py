import pandas as pd


data = pd.read_csv("mushrooms.csv")

#take out values of odor, population, habitat for features -->
feat = data.iloc[:,[5,-2,-1]].values
lab = data.iloc[:,0].values
#impoert  labelEncoder class --> 
from sklearn.preprocessing import LabelEncoder
#OneHotEncoder class
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
#create object of labelEncoder and perform fit transform -->
obj1 = LabelEncoder()
lab = obj1.fit_transform(lab)







#do OneHotEncoding for all columns of feat -->
cTransf = ColumnTransformer([('encoder', OneHotEncoder(), [0,1,2])], remainder = 'passthrough')
# fit transform -->
feat = cTransf.fit_transform(feat).toarray()

#trainig of model -->
from sklearn.model_selection import train_test_split
featTrain,featTest,labTrain,labTest = train_test_split(feat,lab,test_size=0.25,random_state=0)
# import KNeighboursClassifier
from sklearn.neighbors import KNeighborsClassifier
obj2 = KNeighborsClassifier(n_neighbors=5, p=2)
obj2.fit(featTrain,labTrain)
#prediction after training -->
pred = obj2.predict(featTest)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labTest,pred)
#final prediction -->
print ("Accuracy of model: "+str(round(obj2.score(featTest,labTest),3)*100)+"%")


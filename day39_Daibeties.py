import pandas as pd
from sklearn.model_selection import train_test_split

DF=pd.read_csv("diabetes.csv")

#diffrentiate feat and lab before using them 
feat = DF.iloc[:,:-1].values

lab = DF.iloc[:,8].values







#train test split
featTrain,featTest,labTrain,labTest=train_test_split(feat,lab,test_size=0.25,random_state=42)
#import standard scalar from sklearn
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
#fit transform train and test
featTrain = sc.fit_transform(featTrain)
featTest = sc.transform(featTest)

#importing KNeighborsclasifier
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=5, p = 2 , metric = 'minkowski')
classifier.fit(featTrain,labTrain)
labPred = classifier.predict(featTest)

#making the confusion metrics
from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(labPred,labTest)
print(accuracy_score(labPred,labTest),"\n",cm)


from sklearn.metrics import accuracy_score

print("Accuracy:",accuracy_score(labTest, labPred))


classifier.predict([[1,199,72,35,0,28.6,0.627,50]])



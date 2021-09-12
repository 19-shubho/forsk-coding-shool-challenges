import pandas as pd

df = pd.read_csv("addhealth.csv")
df.isnull().any(axis = 0)
for i in df:
    df[i] = df[i].fillna(df[i].mode()[0])
'''
TASK 1: model which checks if an adolescent will smoke or not on basis of a number
of parameters as mentioned in features
'''
#seperate out featutres and labels -->
feat = df[['BIO_SEX','age','WHITE','BLACK','HISPANIC','NAMERICAN','ASIAN',
           'ALCEVR1','ALCPROBS1','marever1','cocever1','inhever1','cigavail',
            'DEP1','ESTEEM1']].values
lab = df["TREG1"].values
    
from sklearn.model_selection import train_test_split as TTS
featTrain,featTest,labTrain,labTest = TTS(feat, lab, test_size = 0.25,
                                    random_state = 0)
from sklearn.linear_model import LogisticRegression
obj1 = LogisticRegression(random_state=0)
obj1.fit(featTrain, labTrain)
#prediction using LR -->
pred = obj1.predict(featTest)

from sklearn.metrics import confusion_matrix
obj1CM = confusion_matrix(labTest, pred)
#accuracy check -->
obj1SCORE = obj1.score(featTest, labTest)
print ("model accuracy-confusion matrix: "+str(obj1CM))
print ("model accuracy-(.score())function: "+str(round(obj1SCORE*100,2)))




'''
TASK 2: model which tells if the adolescent will get expelled or not on basis of
prediction using previous data
'''
#seperate out features and labels -->
featOUT = df[["BIO_SEX","VIOL1"]].values
labOUT = df["EXPEL1"].values

from sklearn.model_selection import train_test_split as TTS
FtTrain,FtTest,LbTrain,LbTest = TTS(featOUT, labOUT, test_size = 0.25,
                                    random_state = 0)
from sklearn.linear_model import LogisticRegression
obj2 = LogisticRegression(random_state=0)
obj2.fit(FtTrain, LbTrain)
#prediction using LR -->
pred1 = obj2.predict(FtTest)

from sklearn.metrics import confusion_matrix
obj2CM = confusion_matrix(LbTest, pred1)

#accuracy check -->
Score1 = obj2.score(FtTest, LbTest)
print ("accuracy-confusion matrix(LR): "+str(obj2CM))
print ("accuracy-(.score() LR): "+str(round(Score1*100,2)))











"""

######## USING KNN ########


from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split as TTS
from sklearn.metrics import confusion_matrix, accuracy_score

# Applying KNN Classifier
classifier_knn = KNeighborsClassifier(n_neighbors = 8)


######## Solution for Part 1 ########

# Separating Dependent and Independent variables as per Problem Statement
fe = df[['BIO_SEX','age','WHITE','BLACK','HISPANIC','NAMERICAN','ASIAN',
           'ALCEVR1','ALCPROBS1','marever1','cocever1','inhever1','cigavail',
           'DEP1','ESTEEM1']].values
la = df["TREG1"].values

# Splitting the Data into Test and Train
FtTrain,FtTest,LbTrain,LbTest = TTS(fe,la,test_size=.2,random_state=0)


classifier_knn.fit(FtTrain,LbTrain)
pred_knn = classifier_knn.predict(FtTest)

# Building Confusion Matrix
CM = confusion_matrix(pred_knn,LbTest)

# Getting Accuracy Score of the Model
Score = accuracy_score(LbTest,pred_knn)
print ("accuracy-confusion matrix(KNN): "+str(CM))
print ("accuracy-.score()(KNN): "+str(round(Score*100,2))+"%")



######## Solution for Part 2 ########

# Separating Dependent and Independent variables as per Problem Statement
fe1 = df[["BIO_SEX","VIOL1"]].values
la1 = df["EXPEL1"].values

# Splitting the Data into Test and Train
ftr,fte,ltr,lte = TTS(fe1,la1,test_size=.2,random_state=0)


classifier_knn.fit(ftr,ltr)
pred1 = classifier_knn.predict(fte)

# Building Confusion Matrix
obj2CM = confusion_matrix(pred1,lte)

# Getting Accuracy Score of the Model
Score1 = accuracy_score(lte,pred1)

print ("accuracy-confusion matrix(KNN): "+str(obj2CM))
print ("accuracy-.score() (KNN): "+str(round(Score1*100,2))+"%"))
"""

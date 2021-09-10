import pandas as pd
data=pd.read_table("amazon_cells_labelled.txt",names=["rev","Liked"])

import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import re

corpus=[]
 
for i in range(0, 1000):
    rev=re.sub('[^a-zA-Z]', ' ', data['rev'][i])
    rev=rev.lower()
    rev=rev.split()
    rev=[word for word in rev if not word in set(stopwords.words('english'))]
    
    ps=PorterStemmer()
    rev=[ps.stem(word) for word in rev]
    rev=' '.join(rev)
    corpus.append(rev)

print(corpus)
print(len(corpus))

from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer(max_feat =1500)
feat=cv.fit_transform(corpus).toarray()
lab=data.iloc[:, 1].values

print(feat.shape)
print(lab.shape)

from sklearn.model_selection import train_test_split
featTrain, featTest, labTrain, labTest=\
train_test_split(feat, lab, test_size=0.20, random_state=0)

#use KNN to your data -->
from sklearn.neighbors import KNeighborsClassifier
obj=KNeighborsClassifier()
# fit KNN throught training set
obj.fit(featTrain, labTrain)

labPred=obj.predict(featTest)

from sklearn.metrics import confusion_matrix
cmKnn=confusion_matrix(labTest, labPred)
print(cmKnn) 
print( (cmKnn[0][0] + cmKnn[1][1]) / (cmKnn[0][0] + cmKnn[1][1] + cmKnn[0][1] + cmKnn[1][0]))

# fiting naive bayes to training set
from sklearn.naive_bayes import GaussianNB
obj=GaussianNB()
obj.fit(featTrain, labTrain)
# now check you prediction -->
labPred=obj.predict(featTest)

from sklearn.metrics import confusion_matrix
cmNb=confusion_matrix(labTest, labPred)
print(cmNb)
print( (cmNb[0][0] + cmNb[1][1]) / (cmNb[0][0] + cmNb[1][1] + cmNb[0][1] + cmNb[1][0]))

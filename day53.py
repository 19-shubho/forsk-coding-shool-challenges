import pandas as pd

df =  pd.read_csv('balanced_reviews.csv.crdownload')
df.isnull().any(axis = 0)
#handle the missing data
df.dropna(inplace =  True)
#remove rating 3 from dataset
df = df [df['overall'] != 3]

import numpy as np
#mark reviews as positive or negative
df['Positivity'] = np.where(df['overall'] > 3 , 1 , 0)

from sklearn.model_selection import train_test_split
featTrain, featTest, labTrain, labTest = train_test_split(df['reviewText'], df['Positivity'], random_state = 42 )

from sklearn.feature_extraction.text import CountVectorizer
vect = CountVectorizer().fit(featTrain)
len(vect.get_feature_names())
vect.get_feature_names()[10000:10010]
featTrain_vectorized = vect.transform(featTrain)

#featTrain_vectorized.toarray()
#create the classifier (first model)
#SVC,KNN, Naive Bayes, Logistic Regression, DT, RF
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(featTrain_vectorized, labTrain)
predictions = model.predict(vect.transform(featTest))
'''
from sklearn.neighbors import KNeighborsClassifier
model2=KNeighborsClassifier()
model2.fit(featTrain, labTrain)
pred2=model2.predict(featTest)
'''
from sklearn.metrics import confusion_matrix
confusion_matrix(labTest, predictions)

from sklearn.metrics import roc_auc_score
roc_auc_score(labTest, predictions)
#roc_auc_score(labTest, pred2)

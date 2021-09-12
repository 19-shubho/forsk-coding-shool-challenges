import pandas as pd

df =  pd.read_csv('balanced_reviews.csv.crdownload')
df.isnull().any(axis = 0)

#handle the missing data
df.dropna(inplace =  True)

#leaving the reviews with rating 3 and collect reviews with
#rating 1, 2, 4 and 5 onyl

df = df [df['overall'] != 3]

import numpy as np

#creating a label
#based on the values in overall column
df['Positivity'] = np.where(df['overall'] > 3 , 1 , 0)

#NLP
#reviewText - feature - df['reviewText']
#Positivity - label - df['Positivity']

#version 02
#tf-idf 
#term frequency inverse document frequency
from sklearn.model_selection import train_test_split
featTrain, featTest, labTrain, labTest = train_test_split(df['reviewText'], df['Positivity'], random_state = 42 )

from sklearn.feature_extraction.text import TfidfVectorizer

vect = TfidfVectorizer(min_df = 5).fit(featTrain)
featTrainVect= vect.transform(featTrain)

#model building
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(featTrainVect, labTrain)
pred = model.predict(vect.transform(featTest))


from sklearn.metrics import confusion_matrix
confusion_matrix(labTest, pred)

from sklearn.metrics import roc_auc_score
roc_auc_score(labTest, pred)


#save - pickle format
#this below code will run on my machine 

import pickle

file  = open("pickle_model.pkl","wb")
pickle.dump(model, file)
#pickle the vocabulary
pickle.dump(vect.vocabulary_, open('features.pkl', 'wb'))
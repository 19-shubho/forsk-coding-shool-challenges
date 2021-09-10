import pandas as pd

df =  pd.read_csv('balanced_reviews.csv.crdownload')
df.shape
df.columns
df.sample(10)
#get the review text coloumn seperated -->
df['reviewText'][0]
df['overall'].value_counts()
# check for any missing data, replace with null -->
df.isnull().any(axis = 0)
df.dropna(inplace =  True)

#discard reviews with rating equal to three -->
df = df [df['overall'] != 3]

import numpy as np
# use np.where function to check if rating > 3 then return 1
# else return 0
df['Positivity'] = np.where(df['overall'] > 3 , 1 , 0)


#NLP begins -->
#feat- df['reviewText']
#lab - df['Positivity']

from sklearn.model_selection import train_test_split

featTrain, featTest, labTrain, labTest = train_test_split(df['reviewText'], df['Positivity'], random_state = 42 )

from sklearn.feature_extraction.text import CountVectorizer
vect = CountVectorizer().fit(featTrain)
len(vect.get_feature_names())

vect.get_feature_names()[10000:10010]
featTrainVect = vect.transform(featTrain)
















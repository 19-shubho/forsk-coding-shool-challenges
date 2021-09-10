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
df.shape
df['Positivity'].value_counts()
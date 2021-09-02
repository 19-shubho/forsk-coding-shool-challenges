# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 10:33:52 2021

@author: Asus
"""

import pandas as pd
df = pd.read_csv('Salaries.csv')

type(df)
df.shape

df.head()

df.tail(2)

df.sample(3)

df['rank']

df['salary']

df['rank']

df[['rank','salary']]

df['rank'].unique()

df['rank'].value_counts(normalize = True)


df['sex'].unique()

df['salary'].max()
df['salary'].min()
df['salary'].mean()

df['salary']
df.salary

df['rank']
df.rank


filter1 = df['salary'] > 100000
df[filter1]


df[df['salary'] > 100000]



df[(df['salary'] > 100000) & (df['sex'] == 'Female')]


df.isnull().any(axis = 0)

df.isnull().any(axis = 1)

df[df.isnull().any(axis = 1)]


df['phd'].mean()

df['phd'] =  df['phd'].fillna(df['phd'].mean())

df2 = df.fillna(100)

df.dropna(inplace = True)

df = pd.read_csv('Salaries.csv')


df.iloc[0:10,2:4]

df.iloc[10,:]

df.iloc[[10,15],:]

df.iloc[:,2]





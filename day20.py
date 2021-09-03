import pandas as pd
import numpy as np

df = pd.read_csv('Baltimore.csv')

df['AnnualSalary'] = df['AnnualSalary'].astype(str)
df['AnnualSalary'] = df['AnnualSalary'].apply(lambda x: x.replace('$',''))
df['AnnualSalary'] = df['AnnualSalary'].astype(float)

grouped = df.groupby(['JobTitle'])['AnnualSalary']
aggregated = grouped.agg([np.sum, np.mean])
print(aggregated)


df['JobTitle'].value_counts()[0:10].plot(kind = 'bar')


agenID = df[['Agency','AgencyID']]
agenID.drop_duplicates(inplace=True)
print(agenID)

ft = df['GrossPay'].isnull()
len(df['GrossPay'][ft])





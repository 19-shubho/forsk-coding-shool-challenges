import re
from glob import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

fl = glob('baby_names/*.txt')
    
LIST = []

for file in fl:
    tmp = pd.read_csv(file, names = ['names','sex','count'])

    yr = int(re.findall('\d\d\d\d', file)[0])
    
    if yr > 2010:
        break

    tmp['yr'] = yr
    LIST.append(tmp)
    
finalDF = pd.concat(LIST, axis = 0, ignore_index = True)

DF2010 = finalDF[finalDF['yr'] ==  2010]

FNames = DF2010[DF2010['sex'] == 'F']

FNames_sort_by_count = FNames.sort_values('count', ascending = False, ignore_index = True)

print (FNames_sort_by_count['names'][0:5]) 


MNames = DF2010[DF2010['sex'] == 'M']

MNames_sort_by_count = MNames.sort_values('count', ascending = False, ignore_index = True)

print (MNames_sort_by_count['names'][0:5]) 

gpdMpl = finalDF.groupby(['yr', 'sex']).agg({'count': ['sum']})

print(gpdMpl)

gpdMpl.plot(kind='bar')

gpdMpl[0:10].plot(kind='bar')
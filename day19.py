import pandas as pd
df=pd.read_csv('titanic.csv')

#num ppl survived
pS=df['Survived'].value_counts()[1]
print('Number of people survived: '+str(pS))

#num ppl dead
pD=df['Survived'].value_counts()[0]
print('Number of people died: '+str(pD))

#calculate survival rates as percentage
pPS=df['Survived'].value_counts(normalize=True)[1]
print('Percentage of people survived is: '+str(round(pPS*100,2))+'%')

pPD=df['Survived'].value_counts(normalize=True)[0]
print('Percentage of people dead is: '+str(round(pPD*100,2))+'%')

#percent males that survived
pMS=df['Survived'][df['Sex'] == 'male'].value_counts(normalize=True)[1]
print('Percentage of males that survived is: '+str(round(pMS*100,2))+'%')

#percent of males dead
pMD=df['Survived'][df['Sex'] == 'male'].value_counts(normalize=True)[0]
print('Percentage of males that dead is: '+str(round(pMD*100,2))+'%')

#percent females that survived
pFS=df['Survived'][df['Sex'] == 'female'].value_counts(normalize=True)[1]
print('Percentage of females that survived is: '+str(round(pFS*100,2))+'%')

#percent of females dead
pFD=df['Survived'][df['Sex'] == 'female'].value_counts(normalize=True)[0]
print('Percentage of females that dead is: '+str(round(pFD*100,2))+'%')

def filter_data(value):
    if 0 <= value <= 18:
        return 1
    else:
        return 0
df['Child'] = df['Age'].apply(filter_data)
c =  df['Survived'][df['Child'] == 1].value_counts(normalize=True)
print ("Child Survived : "+str(round(c[1]*100, 2))+"%")



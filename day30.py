import pandas as pd
import numpy as np
import re

#window 1252 encoding  -->
thnkGiving_DF = pd.read_csv("thanksgiving.csv", encoding="Windows 1252")

#get the coloumn names for future use  -->
colName = thnkGiving_DF.columns.tolist()

print (colName)

#number your coloumn -->
colCode = [x for x in range(0, 65)]

#use codes for coloumns to use them in the dataframe
colNamesMaping = dict(zip(colCode, colName))

#put the codes in datafrsme(initialisation)
thnkGiving_DF.columns = colCode

#data of ppl who celebrate thanksgiving

thnkGiving_DF = thnkGiving_DF[thnkGiving_DF[1] == "Yes"]

#find any empty space
thnkGiving_DF.isnull().any(axis = 0)

#replace empty places with 'Missing' string
thnkGiving_DF = thnkGiving_DF.replace(np.nan, 'Missing')

#region, income, area wise information to be seperated
region = thnkGiving_DF.groupby(64)
print (region.groups)
print (region.size())

income = thnkGiving_DF.groupby(63)
print (income.groups)
print (income.size())

area = thnkGiving_DF.groupby(60) 
print (area.groups)
print (area.size())

#sauce bought by each income grp
saucePref = thnkGiving_DF.groupby(8)[63].value_counts()

print (saucePref)

#specify gender by assigning 0 to male and 1 to female
#use .apply() method
def whichSex(value):
    if value == "Male":
        value = 0
    elif value == "Female":
        value = 1

    return value

thnkGiving_DF[62] = thnkGiving_DF[62].apply(whichSex)
print (thnkGiving_DF[62].value_counts(dropna = False))

#replace income coloumn by missing for those who donot wish to answer
thnkGiving_DF[63] = thnkGiving_DF[63].replace(['Prefer not to answer', 'Missing'],['0','0'])

reg = re.compile("\d+\W*\d+")

def incomeSpecify(value):
    value = reg.findall(value)
    value = [int(x.replace(",", "")) for x in value]
    return sum(value)/(len(value)+0.1)

thnkGiving_DF[63] = thnkGiving_DF[63].apply(incomeSpecify)

#find mean of income w.r.t sauce type
saucePrefByIncome = thnkGiving_DF.groupby(8)[63]

print (saucePrefByIncome.groups)

avgSaucePrefByIncome = saucePrefByIncome.mean()

print (avgSaucePrefByIncome)

# visualisation by plotting a bar graph
avgSaucePrefByIncome.plot.bar()
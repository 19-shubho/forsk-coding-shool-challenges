import pandas as pd

#read the csv file using pandas -->
readDATA=pd.read_csv("Box_Office.csv")

# distinguish features and labels coloumns into NDArrays -->
days=readDATA.iloc[:, 0:1].values
moneyBahubali_Dangal=readDATA.iloc[:, 1:3].values

#import class LinearRegression -->
from sklearn.linear_model import LinearRegression
obj=LinearRegression()
#model training -->
obj.fit(days, moneyBahubali_Dangal) 

day=10

#Collection earned on day 10 --->

Collection=obj.predict([[day]])

bahubaliMoney, dangalMoney=Collection[0]

if bahubaliMoney > dangalMoney:
 print("BAHUBALI 2 MONEY > DANGAL MONEY".format(day))
else:
 print("DANGAL MONEY > BAHUBALI 2 MONEY".format(day))
 
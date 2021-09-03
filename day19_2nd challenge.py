import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Automobile.csv')


#find the data type ofv your column
df['price'].dtype

# change to float type
df['price'] = df['price'].astype(float)

#empty space if any?
df['price'].isnull().any(axis = 0)

# replace with the mean of price coloumn
df['price'] = df['price'].fillna(df['price'].mean())


#price column to ndarray
pNArray = df['price'].values

print ('min price is: '+str(df['price'].min()))
print ('max price is: '+str(df['price'].max()))
print ('avg value of pricew is: '+str(round(df['price'].mean(),2)))
print ('standard deviation of price is: '+str(round(df['price'].std(),2)))


# Make a pie chart for all car makers

series = df['make'].value_counts()

topCarMakers = series.index[0:11]
vehicleCount = series.values[0:11]

plt.pie(vehicleCount, labels=topCarMakers, autopct='%.2f%%')

plt.show()

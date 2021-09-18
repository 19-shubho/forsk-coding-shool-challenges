import requests
from bs4 import BeautifulSoup
#destination link from where data is to be scrapped
destLink = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
# to read html data in text format -->
rdhtml = requests.get(destLink).text
#tool for scrapping data-->
BS = BeautifulSoup(rdhtml, "lxml")
#find your required peice of information from the webpage -->
reqInfo = BS.find('table', class_ = 'wikitable')
#make lists to store each type of info separately from the table
L1 = []
L2 = []
L3 = []
L4 = []
L5 = []
L6 = []
for row in reqInfo.findAll('tr'):
    #get all 'td' rows -->
    row6 = row.findAll('td')
    #get all 'th' rows -->
    row1 = row.findAll('th')
    #skip the first row and do operation on those containing atleast 6 'td'  
    if len(row6) == 6:
        L1.append(row6[1].text.strip())
        L2.append(row1[0].text.strip())
        L3.append(row6[2].text.strip())
        L4.append(row6[3].text.strip())
        L5.append(row6[4].text.strip())
        L6.append(row6[5].text.strip())
import pandas as pd
#now convert your collected data to a DataFrame
df = pd.DataFrame()
df['State'] = L2
df['AdminisCap'] = L1
df['LegCap'] = L3
df['JudCap'] = L4
df['Year'] = L5
df['FormerCap'] = L6        

df.to_csv('tableDataBeautifulSoup.csv', index = False)

df1 = pd.DataFrame(zip(L1,L2,L3,L4,L5,L6), columns = ['States','L2','L3','L4','L5','L6'])       
 
    
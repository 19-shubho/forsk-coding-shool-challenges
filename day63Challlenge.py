destLink = 'https://www.embibe.com/exams/nirf-rankings/'

import requests

rdhtml = requests.get(destLink).text

from bs4 import BeautifulSoup

BS = BeautifulSoup(rdhtml,'lxml')

#find all tables with class name 'wp-block-table' -->
tables = BS.find_all('table', class_ = 'wp-block-table')
#make a list that will hold all four tables at one place -->
tablesFour = ['nirf overall.csv', 'nirf engineering.csv', 'nirf medical.csv', 'nirf universities'] 

for i in range(len(tables)):
    l1 = []
    l2 = []
    l3 = []
    l4 = []

    for body in tables[i].find_all('tbody'):
        #in all 'tr' rows -->
        for row in tables.findall('tr'):
            #get all 'td' coloumns -->
            row4=row.find_all('td')
            l1.append(row4[0].text.strip())
            l2.append(row4[1].text.strip())
            l3.append(row4[2].text.strip())
            l4.append(row4[3].text.strip())
    
    import pandas as pd
    df = pd.DataFrame()
    #make the respective columns of newly created dataframe -->
    df['rank & name of institute'] = l1
    df['city'] = l2
    df['state'] = l3
    df['nirf score'] = l4
    #make a master csv file -->
    df.to_csv(tablesFour[i], index = False)

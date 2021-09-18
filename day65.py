from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

url = "http://keralaresults.nic.in/sslc2019duj946/swr_sslc.htm"

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get(url)

sleep(2)

scCode =driver.find_element_by_name('treg')

scCode.send_keys('2000')

sleep(2)

scResult =driver.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[3]/td[3]/input[1]')
scResult.click()


remoteSiteHTML =driver.page_source


from bs4 import BeautifulSoup as BS


soup = BS(remoteSiteHTML)


driver.quit()


wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

driver.get(wiki)

right_table = driver.find_element_by_class_name('wikitable')

A = []
B = []
C = []
D = []
E = []
F = []

for row in right_table.find_elements_by_tag_name('tr'):
    cells = row.find_elements_by_tag_name('td')
    states = row.find_elements_by_tag_name('th')
    
    #if it is first row, th(count) = 7, td(count) = 0
    #for rest of rows, th(count) = 1, td(count) = 6
    
    if len(cells) == 6:
        A.append(cells[1].text.strip())
        B.append(states[0].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        E.append(cells[4].text.strip())
        F.append(cells[5].text.strip())
        
        
import pandas as pd


df = pd.DataFrame()

df['State_UT'] = B
df['Admin_Cap'] = A
df['Legis_Cap'] = C
df['Judi_Cap'] = D
df['Year'] = E
df['Formar_Cap'] = F

# -*- coding: utf-8 -*-

from selenium import webdriver

from bs4 import BeautifulSoup
url = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
driver = webdriver.Chrome("C:/Users/lenovo/Desktop/my_repo/python_web_scrapping/chromedriver.exe")
sourse=driver.get(url)
soup=BeautifulSoup(sourse)

right_table=soup.find('table', class_='wikitable')

print (right_table)



A=[]
B=[]
C=[]
D=[]
E=[]
F=[]

for row in right_table.findAll("tr"):
    cells = row.findAll('td')
    states=row.findAll('th') 
    if len(cells)==5: 
        A.append(cells[0].text.strip().replace("\xa0"," "))
        B.append(states[1].text.strip())
        C.append(cells[1].text.strip())
        D.append(cells[2].text.strip())
        E.append(cells[3].text.strip())
        F.append(cells[4].text.strip())
        
import pandas as pd
df=pd.DataFrame(A,columns=['Number'])
df['State/UT']=B
df['Admin_Capital']=A
df['Legislative_Capital']=C
df['Judiciary_Capital']=D
df['Year_Capital']=E
df["Former_Capital"] = F
df.to_csv("vidhan.csv")




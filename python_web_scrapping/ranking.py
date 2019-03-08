# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 10:37:48 2019

@author: lenovo
"""

from bs4 import BeautifulSoup
import requests
url="https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
sourse=requests.get(url).text
soup=BeautifulSoup(sourse)
all_tables=soup.find_all("table")

right_table=soup.find('table', class_='table-body')

print (right_table)
A=[]
B=[]
C=[]
D=[]


for row in right_table.findAll("tr"):
    cells = row.findAll("tr")
    
    if len(cells)==5: 
        A.append(cells[0].text.strip().replace("\xa0"," "))
        B.append(cells[1].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
       
import pandas as pd
df=pd.DataFrame(A,columns=['Number'])
df['weighted matches']=B
df['team']=A
df['points']=C
df['ratings']=D

df.to_csv("former.csv")
        






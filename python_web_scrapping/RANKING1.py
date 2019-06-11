# -*- coding: utf-8 -*-
"""
Created on Wed May 22 22:33:56 2019

@author: lenovo
"""

from bs4 import BeautifulSoup
import requests
wiki="https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
sourse=requests.get(wiki).text
soup=BeautifulSoup(sourse)
all_table=soup.find_all("table")
right_table=soup.find('table',class_='table')
print(right_table)
A=[]
B=[]
C=[]
D=[]
E=[]

for row in right_table.findAll("tr"):
    cells=row.findAll("td")
    
    if len(cells)==5:
        A.append(cells[0].text.strip().replace("\xa0"," "))
        B.append(cells[1].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        E.append(cells[4].text.strip())
   
import pandas as pd
df=pd.DataFrame(A,columns=["number"])
df["team"]=B
df["weight matches"]=C
df["points"]=D
df["ratings"]=E
df.to_csv("vidhan.csv")
df.iloc[0:2,-1].values
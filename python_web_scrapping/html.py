# -*- coding: utf-8 -*-
"""
Created on Thu May 23 07:18:30 2019

@author: lenovo
"""

from bs4 import BeautifulSoup
import requests
wiki="https://www.w3schools.com/html/html_tables.asp"
sourse=requests.get(wiki).text
soup=BeautifulSoup(sourse)
A=[]
B=[]
C=[]
all_table=soup.findAll("table")
right_table=soup.find("div",class_="w3-white")
print(right_table)
rt_table = right_table.find("table")




for row in rt_table.findAll('tr'):
    cells=row.findAll('td')
    if len(cells)==3:
        A.append(cells[0].text.strip().replace("\xa0"," "))
        B.append(cells[1].text.strip())
        C.append(cells[2].text.strip())
        
        
import pandas as pd
df=pd.DataFrame(A,columns=["company"])
df["contact"]=B
df["country"]=C


df.to_csv("html.csv")
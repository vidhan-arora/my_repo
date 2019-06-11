# -*- coding: utf-8 -*-
"""
Created on Fri May 24 08:36:28 2019

@author: lenovo
"""


from selenium import webdriver

wiki="https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
driver = webdriver.Chrome("C:/Users/lenovo/Downloads/chromedriver.exe")
driver.get(wiki)
right_table=driver.find_element_by_class_name('table')
A=[]
B=[]
C=[]
D=[]
E=[]
for row in right_table.find_elements_by_tag_name("tr"):
    cells = row.find_elements_by_tag_name("td")
    if len(cells)==5:
         A.append(cells[0].text)
         B.append(cells[1].text)
         C.append(cells[2].text)
         D.append(cells[3].text)
         E.append(cells[4].text)
import pandas as pd
df=pd.DataFrame(A,column=["position"])
df["team"]=B
df["wm"]=C
df["points"]=D
df["rating"]=E
df.to_csv("selenium_rating.csv")

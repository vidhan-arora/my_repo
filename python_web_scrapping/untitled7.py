# -*- coding: utf-8 -*-
"""
Created on Fri May 24 10:32:11 2019

@author: lenovo
"""

from selenium import webdriver
wiki="https://www.w3schools.com/html/html_tables.asp"
driver = webdriver.Chrome("C:/Users/lenovo/Downloads/chromedriver.exe")
driver.get(wiki)
right_table=driver.find_element_by_class_name('w3-white')
A=[]
B=[]
C=[]
for row in right_table.find_elements_by_tag_name("tr"):
    cells = row.find_elements_by_tag_name("td")
    if len(cells)==3:
         A.append(cells[0].text)
         B.append(cells[1].text)
         C.append(cells[2].text)
import pandas as pd
df=pd.DataFrame(A,column=["company"])
df["contact"]=B
df["contry"]=C
df.to_csv("selenium_html.csv")
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 17:57:33 2019

@author: lenovo
"""

from bs4 import BeautifulSoup     
import requests
wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
source = requests.get(wiki).text
soup = BeautifulSoup(source,"lxml")
right_table=soup.find("h1", class_="firstHeading")   
print(right_table.text)
para=soup.findAll("p")[1]
print(para)
content=soup.find(id="toc",class_="toc")
print(content.text)
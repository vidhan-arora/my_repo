# Web Scraping with BeautifulSoup and Requests

# Parsing the content from the website and
# pulling  the exact information you want
# Introduce to the page for Web Scrapping

# pip install beautifulsoup4
# pip install lxml
# pip install html5lib

"""
Introduce the concept of basic HTML tags
HTML
  HEAD

  HEAD

  BODY

  BODY
HTML

"""

from bs4 import BeautifulSoup
import requests

# Create simple html files and
# parse that using bs4 to make the students understand with title, div etc

with open("data/simple.html") as html_file :
  soup = BeautifulSoup(html_file, "lxml")

print (soup)

print (soup.prettify())

print (soup.title)

print (soup.title.text)

print (soup.div)

print (soup.div.h1.text)

# Crome browser ( use the inspect tool to use the find function )
match = soup.find('div')
print (match)

match = soup.find("div", class_= "footer")
print (match)

print ( match.h2 )
print ( match.h2.text )

print ( match.p )
print ( match.p.text )

for article in soup.find_all("div") :
  headline = article.p.text
  print (headline)

# Give students a challenge to print some information from the HTML pages




# Reading from the Internet
from bs4 import BeautifulSoup
source = requests.get("http://httpbin.org/html").text
soup = BeautifulSoup(source,"lxml")

print (soup.prettify())

print (soup.head)

print (soup.body)

print (soup.body.h1)

print (soup.body.div)

print (soup.body.div.p)

print (soup.body.div.p)



# Web Scrapping a real Page

#import the Beautiful soup functions to parse the data returned from the website
from bs4 import BeautifulSoup     
import requests
import unicodedata



#specify the url
wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
source = requests.get(wiki).text
soup = BeautifulSoup(source)



print (soup.prettify())

all_tables=soup.find_all('table')

print (all_tables)

right_table=soup.find('table', class_='wikitable')

print (right_table)


#Generate lists
A=[]
B=[]
C=[]
D=[]
E=[]
F=[]

for row in right_table.findAll("tr"):
    cells = row.findAll('td')
    states=row.findAll('th') #To store second column data
    if len(cells)==6: #Only extract table body 'not heading
        A.append(cells[0].text.strip().replace("\xa0"," "))
        B.append(states[0].text.strip())
        C.append(cells[1].text.strip())
        D.append(cells[2].text.strip())
        E.append(cells[3].text.strip())
        F.append(cells[4].text.strip())
        


#import pandas to convert list to data frame
import pandas as pd
df=pd.DataFrame(A,columns=['Number'])
df['State/UT']=B
df['Legislative_Capital']=A
df['Admin_Capital']=C
df['Judiciary_Capital']=D
df['Year_Capital']=E
df["Former_Capital"] = F
df.to_csv("former.csv")
#print (df)



"""
Code Challenge
  Name:
    Webscrapping ICC Cricket Page
  Filename:
    icccricket.py
  Problem Statement:
    Write a Python code to Scrap data fro0m ICC Ranking's
    page and get the ranking table for ODI's (Men).
    Create a DataFrame using pandas to store the information.
  Hint:
    https://www.icc-cricket.com/rankings/mens/team-rankings/odi
"""

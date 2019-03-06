import pandas as pd
from selenium import webdriver

wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"


#driver = webdriver.Firefox(executable_path=r'C:/Users/hp/Downloads/geckodriver')
driver = webdriver.Chrome("C:/Users/pc/Downloads/chromedriver_win32/chromedriver.exe")

driver.get(wiki)    # Opening the submission url



right_table=driver.find_element_by_class_name('wikitable')


#Generate lists
A=[]
B=[]
C=[]
D=[]
E=[]
F=[]

for row in right_table.find_elements_by_tag_name("tr"):
    cells = row.find_elements_by_tag_name("td")
    states=row.find_elements_by_tag_name("th") #To store second column data
    if len(cells)==5: #Only extract table body not heading
        A.append(str(cells[0].text))
        B.append(str(states[1].text))
        C.append(str(unicodedata.normalize('NFKD', cells[1].text).encode('ascii','ignore')))
        D.append(str(unicodedata.normalize('NFKD', cells[2].text).encode('ascii','ignore')))
        E.append(str(cells[3].text))
        F.append(str(unicodedata.normalize('NFKD', cells[4].text).encode('ascii','ignore')))



#import pandas to convert list to data frame                                   
"""import pandas as pd
df=pd.DataFrame(A,columns=['Number'])
df['State/UT']=B
df['Admin_Capital']=A
df['Legislative_Capital']=C
df['Judiciary_Capital']=D
df['Year_Capital']=E
df["Former_Capital"] = F
df.to_csv("former.csv")
#print (df)
"""
driver.quit()



#Real website data scrapping for Kerela Results

from  selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup as BS

url = "http://keralaresults.nic.in/sslc2018rgr8364/swr_sslc.htm"
browser = webdriver.Chrome("C:/Users/lenovo/Desktop/my_repo/python_web_scrapping/chromedriver.exe")
browser.get(url)


sleep(2)


school_code = browser.find_element_by_name("treg")
code="2002"
school_code.send_keys(code)


sleep(2)


get_school_result = browser.find_element_by_xpath('//*[@id="ctrltr"]/td[3]/input[1]')    
get_school_result.click()


sleep(5)                                                                       

html_page = browser.page_source

soup = BS(html_page)


sleep(3)


browser.quit()

# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 16:16:29 2019

@author: lenovo
"""

import pandas as pd
df=pd.read_csv("Baltimore_City_Employee_Salaries_FY2014.csv")
df.groupby(['JobTitle','AnnualSalary']).mean()
df.groupby(['JobTitle','AnnualSalary']).max()
df.groupby(['JobTitle','AnnualSalary']).min()
df_sorted=df.sort_values(by=['AnnualSalary']).tail(1)
print(df_sorted)
df1=df.groupby(['JobTitle'].sort_values(by=['JobTitle'],ascending=[True]))
df1_sorted=df.sort_values(by=['JobTitle'],ascending=[True])

rdf=list(df['GrossPay'][df['GrossPay'].isnull()==True].index)
print(rdf)
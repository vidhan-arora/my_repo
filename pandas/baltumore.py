# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 16:16:29 2019

@author: lenovo
"""
Code Challenge
  Name: 
    Baltimore City Analysis
  Filename: 
    baltimore.py
  Problem Statement:
    Read the Baltimore_City_Employee_Salaries_FY2014.csv file 
    and perform the following task :

    
    0. remove the dollar signs in the AnnualSalary field and assign it as a float
    0. Group the data on JobTitle and AnnualSalary, and aggregate with sum, mean, etc.
       Sort the data and display to show who get the highest salary
    0. Try to group on JobTitle only and sort the data and display
    0. How many employess are there for each JobRoles
        0. List All the Agency ID and Agency Name 
    0. Find all the missing Gross data in the dataset 


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
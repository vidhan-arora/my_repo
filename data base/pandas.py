# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 17:06:09 2019

@author: lenovo
"""

"""
Code Challenge
  Name: 
    Titanic Analysis
  Filename: 
    titanic.py
  Problem Statement:
      It’s a real-world data containing the details of titanic ships 
      passengers list.
      Import the training set "training_titanic.csv"
  Answer the Following:
      How many people in the given training set survived the disaster ?
      How many people in the given training set died ?
      Calculate and print the survival rates as proportions (percentage) 
      by setting the normalize argument to True.
      Males that survived vs males that passed away
      Females that survived vs Females that passed away
      
      Does age play a role?
      since it's probable that children were saved first. 
      
      Another variable that could influence survival is age; 
      since it's probable that children were saved first.

      You can test this by creating a new column with a categorical variable Child. 
      Child will take the value 1 in cases where age is less than 18, 
      and a value of 0 in cases where age is greater than or equal to 18.
        
      To add this new variable you need to do two things

        1.     create a new column, and

        2.     Provide the values for each observation (i.e., row) based on the age of the passenger.


      
  Hint: 
      To calculate this, you can use the value_counts() method in 
      combination with standard bracket notation to select a single column of
      a DataFrame
      
      You can test this by creating a new column with a categorical variable Child.
      Child will take the value 1 in cases where age is less than 18, 
      and a value of 0 in cases where age is greater than or equal to 18.  

      Then assign the value 0 to observations where the passenger 
      is greater than or equal to 18 years in the new Child column.
      Compare the normalized survival rates for those who are <18 and 
      those who are older. 
   
"""


"""
Code Challenge
  Name: 
    Automobile Analysis
  Filename: 
    automobile.py
  Problem Statement:
    Read the Automobile.csv file and perform the following task :
    1. Handle the missing values for Price column
    2. Get the values from Price column into a numpy.ndarray
    3. Calculate the Minimum Price, Maximum Price, Average Price and Standard Deviation of Price
"""


On Mon, Feb 25, 2019 at 4:24 PM Forsk Labs <forsklabs@gmail.com> wrote:
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 17:32:25 2018

@author: Forsk
"""

#Import Pyacthon Libraries

import pandas as pd


#Read csv file
df = pd.read_csv("automobile.csv")

#List first 5 records
df.head(9)

#Try to read the first 10, 20, 50 records;
#Can you guess how to view the last few records;

df.tail(7)

#Check types for all the columns
df.dtypes
df.columns #list the column names
df.axes #list the row labels and column names
df.ndim   #number of dimensions
df.size #number of elements
df.shape #return a tuplerepresenting the dimensionality
df.values #numpyrepresentation of the data

df.describe() #generate descriptive statistics (for numeric columns only)

df.max() #return max/minvalues for all numeric columns
df.min()

df.mean()
df.median()
df.std()

df.sample(7) #returns a random sample of thedata frame

#What are the mean values of the first 50 records in the dataset?
df.head(10).mean()

"""
Selecting a column in a Data Frame
Method 1: Subset the data frame using column name:
df['sex']
Method 2: Use the column name as an attribute:
df.sex
Note:there is an attribute rankfor pandas data frames, 
so to select a column with a name "rank" we should use method 1.
"""

df["length"]
df.phd
df.rank

df['price']
df[['price','length']]
df['length'].value_counts()

#calculate the basic statstics on the salary column
df['price'].mean()
df['price'].describe()

#Find how many values in the salarycolumn (use countmethod);
df['price'].count()

#calculate the avg salary
print (df['price'].mean())       

"""
Data Frames groupbymethod

Using "group by" method we can:
•Split the data into groups based on some criteria
•Calculate statistics (or apply a function) to each group

"""
#Group data using rank
df_rank= df.groupby(['num_cylinders'])
#Calculate mean value for each numeric column per each group
df_rank.mean()

#group data using rank followed  by

df.groupby(['length', 'num_cylinders']).mean()


#Calculate mean salary for each professor rank:
df.groupby('rank')[['salary','phd']].mean()


"""
groupbyperformance notes:
-no grouping/splitting occurs until it's needed. 
Creating the groupby object only verifies that you have passed 
a valid mapping
-by default the group keys are sorted during the 
groupby operation. You may want to pass sort=False 
for potential speedup:
"""
#Calculate mean salary for each professor rank:
df.groupby(['rank'],sort=False)[['salary']].mean()
df.groupby(['rank'],sort=False)[['salary']].sum()
"""
Data Frame: filtering

To subset the data we can apply Boolean indexing. 
This indexing is commonly known as a filter. 
For example if we want to subset the rows in which the salary
 value is greater than $120K:
"""
#select only those professors who has salary more than 120000
df_sub= df[["length","num_cylinders"]][(df['price'] > 120000) ]

df_sub= df[(df['salary'] > 120000) ][["rank","phd"]]
#filter using multiple columns

df_sub= df[(df['salary'] > 120000) & \
           (df['phd'] > 10) & \
           (df['sex'] == 'Female' )]

#Select only those rows that contain female professors:

S1 = df[df['sex'] == 'Female' ]['salary']
DF1 = pd.DataFrame(S1)
"""
merging 

"""



"""
Data Frames: Slicing

When selecting one column, it is possible to use single set of 
brackets, but the resulting object will be a Series (not a DataFrame)


When we need to select more than one column and/or make the 
output to be a DataFrame, we should use double brackets

"""

#Select column salary:
df['salary']
df["salary"]

#Select column salary:
df[['rank','salary']]

"""
Data Frames: method loc

If we need to select a range of rows, using their labels 
we can use method loc
"""
df.loc[10:20,['rank','sex']]
df.loc[10:]
"""
Data Frames: method iloc

If we need to select a range of rows and/or columns, 
using their positions we can use method iloc
"""
df.iloc[2:10,[0,2, 3]]


df.iloc[0] # First row of a data frame

df.iloc[1:5, :-1] # Leave last columns

df.iloc[:, 0] # First column

df.iloc[:, -1] # Last column

df.iloc[0:7] #First 7 rows

df.iloc[:, 0:2] #First 2 columns

df.iloc[1:3, 0:2] #Second through third rows and first 2 columns

df.iloc[[0,5], [1,3]] #1stand 6throws and 2ndand 4thcolumns

"""
DataFrame sorting
"""

# Create a new data frame from the original sorted by the column Salary
df_sorted= df.sort_values( by='service')
df_sorted.head()

#We can sort the data using 2 or more columns:
df_sorted= df.sort_values( by=['service','salary'], ascending = [True,True])
df_sorted.head(10)

df_sorted= df.sort_values( by=['service','salary'], ascending = [False,False])
df_sorted.head(5)


"""
Missing Values

Missing values are marked as NaN
"""

# Read a dataset with missing values
import pandas as pd
salary = pd.read_csv("Salaries.csv")


#return a matrix by checking individual values
salary.isnull()

#which column has null values
salary.isnull().any(axis=0)
#OR
salary.isnull().any()

#Check the rows that has atleast one NaN values
salary.isnull().any(axis=1)

# Select the rows that have at least one missing value
salary[salary.isnull().any(axis=1)]

salary[salary.isnull().any(axis=1)].head(2)


#There are a number of methods to deal with missing values in the data frame:
new_df = salary.dropna()

"""
dropna(how='all') >> Drop observations where all cells is NA
dropna(axis=1, how='all') >> Drop column if all the values aremissing
dropna(thresh = 5) >> Drop rows that contain less than 5 non-missing values
fillna(0) >> Replace missing values with zeros
isnull() >> returns True if the value is missing
notnull() >> Returns True for non-missing values

More notes:
    Missing Values

•When summing the data, missing values will be treated as zero
•If all values are missing, the sum will be equal to NaN
•cumsum() and cumprod() methods ignore missing values but 
preserve them in the resulting arrays
•Missing values in GroupBymethod are excluded (just like in R)
•Many descriptive statistics methods have skipnaoption to control 
if missing data should be excluded . This value is set to True by 
default (unlike R)

"""

"""
some advanced analytics
https://www.kdnuggets.com/2017/06/7-steps-mastering-data-preparation-python.html
"""

salary = pd.read_csv("Salaries.csv")

"""
#for back fill 

train.fillna(method='bfill')
#for forward-fill

train.fillna(method=''ffill)

#one can also specify an axis to propagate (1 is for rows and 0 is for columns)

train.fillna(method='bfill', axis=1)
"""

#forward fill
salary = salary.fillna(method='ffill')

#backward fill

salary = salary.fillna(method='bfill')

#hard coded values
salary = salary.fillna(100)

# fill all the records with missing values, with mean of that column
salary['phd'] = salary['phd'].fillna(salary['phd'].mean())
# All columns
salary = salary.fillna(salary.mean())

method='bfill'

salary['rank'] = salary['rank'].fillna(salary['rank'].value_counts().index[0])


#agg() method are useful when multiple statistics are computed per column:
salary[['service','salary']].agg(['min','mean', 'median', 'sum'])


#----------------
#code challenges
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 12:24:40 2017

@author: Kunal
"""

"""
Ref:
https://github.com/TarekDib03/titanic-EDA/blob/master/Titanic%20-%20Project.ipynb
https://www.kaggle.com/rounak15/titanic-survival-prediction-with-python
"""

"""
Python hand boook
https://github.com/jakevdp/PythonDataScienceHandbook/tree/master/notebooks
"""

import pandas as pd

data = pd.read_csv('training_titanic.csv')
data['Child'] = 0
print "Total Survived",data["Survived"].value_counts(normalize=True)[1]

m =  data['Survived'][data['Sex'] == 'male'].value_counts(normalize=True)
print "Males Survived",m[1]

f =  data['Survived'][data['Sex'] == 'female'].value_counts(normalize=True)
print "Females Survived",f[1]








data['Child'][data['Age'] < 18] = 1


c =  data['Survived'][data['Child'] == 1].value_counts(normalize=True)
print "Child Survived",c[1]




#few assignments

import re 
import pandas as pd


data = {'raw': ['TZOV42x34F1-020-0223']}
df = pd.DataFrame(data, columns = ['raw'])
df



# In the column 'raw', extract single digit in the strings

df['col1'] = df['raw'].str.extract('(\w\w)', expand=True)
df['col1']

df['col2'] = df['raw'].str.extract('((?<=^..)[\w]{2})', expand=True)
df['col2']

df['col3'] = df['raw'].str.extract('((?<=^....)[\d]{1,}x[\d]{1,})', expand=True)
df['col3']

df['col4'] = df['raw'].str.extract('(\w\d(?=-\d{1,}))', expand=True)
df['col4']

df['col5'] = df['raw'].str.extract('(\d{1,}(?=-\d{1,}$))', expand=True)
df['col5']

df['col6'] = df['raw'].str.extract('(\d{1,}$)', expand=True)
df['col6']


#version2

str1 = 'TZOV4x3F1-020-022'








print [re.match('(\w{2})', str1).groups()[0]]

print re.findall('((?<=^..)[\w]{2})', str1)

print re.findall('((?<=^....)[\w]{3})', str1)

print re.findall('((?<=^[\w]{7})[\w]{2})', str1)

print [re.findall('(\d\d\d)', str1)[0]]

print [re.findall('(\d\d\d)', str1)[1]]




"""
Flattening JSON objects in Python

"""

sample_object = {
                    'Name':'John',
                    'Location':{'City':'Los Angeles','State':'CA'},
                }

from pandas.io.json import json_normalize
dataframe = json_normalize(sample_object)

"""
Flattening an object with embedded arrays
"""

sample_object2 = {
                    'Name':'John',
                    'Location':{'City':'Los Angeles','State':'CA'},
                    'Hobbies':['Running', 'Music', 'Programming']
                }

df2 = json_normalize(sample_object2)

"""
Using a recusrive function to flatten an object of arbitrary structure
"""
def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[str(name[:-1])] = str(x)

    flatten(y)
    return out

flat = flatten_json(sample_object2)
print flat

df3 = json_normalize(flat)


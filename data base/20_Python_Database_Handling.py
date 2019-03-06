#Database Handling ( sqlite, mysql, mongodb and mlab )


# Database handling using sqlite 

import os                                        
import sqlite3
from pandas import DataFrame                                                   

#os.chdir('/Users/sylvester/Desktop/Database and Python/Python/')


# In memory based database 
conn = sqlite3.connect ( ' :memory: ' )

# File based database ( connects if exits or creates a new one if it does not exists ) 
conn = sqlite3.connect ( 'employee.db' )


# creating cursor
c = conn.cursor()


# STEP 1
# www.sqlite.org/datatype3.html
c.execute ("""CREATE TABLE employees(
          id INTEGER,
          first  TEXT,
          last TEXT,
          pay INTEGER             
          )""")


# STEP 2
c.execute("INSERT INTO employees VALUES (01,'Sylvester', 'Fernandes', 50000)")
c.execute("INSERT INTO employees VALUES (02,'Yogendra', 'Singh', 70000)")
c.execute("INSERT INTO employees VALUES (03,'Rohit', 'Mishra', 30000)")
c.execute("INSERT INTO employees VALUES (04,'Kunal', 'Vaid', 30000)")
c.execute("INSERT INTO employees VALUES (05,'Devendra', 'Shekhawat', 30000)")


# STEP 3
c.execute("SELECT * FROM employees")
# "SELECT * FROM employees WHERE last = 'Fernandes' "



# STEP 4
# returns one or otherwise None as a tuple
print ( c.fetchone()) 

# returns one or otherwise None as a tuple
print ( c.fetchmany(2)) 

# returns a list of tuples
print ( c.fetchall() )


# Since now the cursor has read all the rows and we are at End
# So again fetching the records from the database
c.execute("SELECT * FROM employees")


# STEP 5
df = DataFrame(c.fetchall())  # putting the result into Dataframe
df.columns = ["id","first","last","pay"]


# STEP 6
# commits the current transaction 
conn.commit()

# STEP 7
# closing the connection 
conn.close()







# Database handling using MySQL on Local Machine
#use below command in anaconda prompt
# conda install mysql-connector
# pip install --upgrade pip 
# pip install -U setuptools
# pip install -U wheel
# pip install protobuf
# pip install mysql-connector-python-rf
#pip install argparse

from pandas import DataFrame
import mysql.connector



# File based database ( connects if exits or creates a new one if it does not exists ) 
conn = mysql.connector.connect ( user='root', password='Rocks95@', host='localhost')
# database = '' can be used if we want to connect to already defined database


# creating cursor
c = conn.cursor()

# STEP 0
c.execute("DROP DATABASE employee;")

# STEP 1
c.execute("CREATE DATABASE employee;")

# STEP 2
c.execute("USE employee;")

# STEP 3
c.execute ("""CREATE TABLE employees(
          id INTEGER,
          first  TEXT,
          last TEXT,
          pay INTEGER
          )""")


# STEP 4
c.execute("INSERT INTO employees VALUES (01,'Sylvester', 'Fernandes', 50000)")
c.execute("INSERT INTO employees VALUES (02,'Yogendra', 'Singh', 70000)")
c.execute("INSERT INTO employees VALUES (03,'Rohit', 'Mishra', 30000)")
c.execute("INSERT INTO employees VALUES (04,'Kunal', 'Vaid', 30000)")
c.execute("INSERT INTO employees VALUES (05,'Devendra', 'Shekhawat', 30000)")

# c.execute("INSERT INTO employee VALUES ({},'{}', '{}', {})".format(idd, first,last,pay))


c.execute("SELECT * FROM employees")

# STEP 5
# returns one or otherwise None as a tuple
print ( c.fetchone()) 

# returns one or otherwise None as a tuple
print ( c.fetchmany(2)) 

# returns a list of tuples
print ( c.fetchall() )


# Since now the cursor has read all the rows and we are at End
# So again fetching the records from the database
c.execute("SELECT * FROM employees")



# STEP 6
df = DataFrame(c.fetchall())  # putting the result into Dataframe
df.columns = ["id","first","last","pay"]

# field_names = [i[0] for i in c.description]
# print field_names





# Database handling using MySQL on Cloud

"""
https://www.db4free.net
https://www.db4free.net/phpMyAdmin/
MySQL Host Name : db4free.net
Port : 3306
MySQL database name:  forsk_test
MySQL username: forsk_root
MySQL user password: cooler2112 
Email address:  sylvester@forsk.in
MYSQL URL : mysql://forsk_root:cooler2112@db4free.net/forsk_test

"""


import mysql.connector 
# connect to  MySQL server along with Database name

conn = mysql.connector.connect(user='forsk_root', password='cooler2112',
                              host='db4free.net', database = 'forsk_test')
#, database = 'forsk_test'

# creating cursor
c = conn.cursor()

# STEP 0
#c.execute("DROP DATABASE employee;")

# STEP 1
#c.execute("CREATE DATABASE employee;")

# STEP 2
c.execute("DROP Table employees;")

# STEP 3
c.execute ("""CREATE TABLE employees(
          id INTEGER,
          first  TEXT,
          last TEXT,
          pay INTEGER
          )""")


# STEP 4
c.execute("INSERT INTO employees VALUES (01,'Sylvester', 'Fernandes', 50000)")
c.execute("INSERT INTO employees VALUES (02,'Yogendra', 'Singh', 70000)")
c.execute("INSERT INTO employees VALUES (03,'Rohit', 'Mishra', 30000)")
c.execute("INSERT INTO employees VALUES (04,'Kunal', 'Vaid', 30000)")
c.execute("INSERT INTO employees VALUES (05,'Devendra', 'Shekhawat', 30000)")

# c.execute("INSERT INTO employee VALUES ({},'{}', '{}', {})".format(idd, first,last,pay))


c.execute("SELECT * FROM employees")


# STEP 5
# returns one or otherwise None as a tuple
print ( c.fetchone()) 

# returns one or otherwise None as a tuple
print ( c.fetchmany(2)) 

# returns a list of tuples
print ( c.fetchall() )


# Since now the cursor has read all the rows and we are at End
# So again fetching the records from the database
c.execute("SELECT * FROM employees")


# STEP 6
df = DataFrame(c.fetchall())  # putting the result into Dataframe
df.columns = ["id","first","last","pay"]




# Database handling using MongoDB locally 
#use below command in anaconda prompt
#pip install pymongo


from pymongo import MongoClient

client = MongoClient('localhost', 27017)

# create the database if does not exists
mydb = client.employee



# adding the employee in the employee collection
def add_employee(idd, first, last, pay):
    unique_employee = mydb.employees.find_one({"id":idd})
    if unique_employee:
        return "Employee already exists"
    else:
        mydb.employees.insert(
                {
                "id" : idd,
                "first" : first,
                "last" : last,
                "pay" : pay
                })
        return "Employee added successfully"

def fetch_all_employee():
    user = mydb.employees.find()
    for i in user:
        print (i)



add_employee(01,'Sylvester', 'Fernandes', 50000)
add_employee(02,'Yogendra', 'Singh', 70000)
add_employee(03,'Rohit', 'Mishra', 30000)
add_employee(04,'Kunal', 'Vaid', 30000)
add_employee(05,'Devendra', 'Shekhawat', 30000)

fetch_all_employee()
    




# Database handling using MongoDB on Cloud ( mLab )
# Steps to create DB and Account online mLab

import requests
import json
api_key = "65mczz6BHJHLMxUayNO2VXNYWedu11q4"
collection = "employee"
database = "employees"

data_dict = {}

# adding the employee in the employee collection
def add_employee(idd, first, last, pay):
  
  data_dict = {"id" : idd,"first" : first,"last" : last,"pay" : pay}
  add_data_to_mlab(data_dict)
        
        

res = ""
def add_data_to_mlab(data_dict):
    
    url = "https://api.mlab.com/api/1/databases/{}/collections/{}?apiKey={}".format(database,collection,api_key)
    response = requests.post(url, json =data_dict)
    
    res = response.status_code
    if res == 200:
        print "data added successfully"
    else:
        print "response is something else:"
        print res



    
def fetch_all_employee():
    
    url = "https://api.mlab.com/api/1/databases/{}/collections/{}?apiKey={}".format(database,collection,api_key)
    response = requests.get(url)
    
    res = json.loads(response.text)
    print res
    
    
    
    
add_employee(01,'Sylvester', 'Fernandes', 50000)
add_employee(02,'Yogendra', 'Singh', 70000)
add_employee(03,'Rohit', 'Mishra', 30000)
add_employee(04,'Kunal', 'Vaid', 30000)
add_employee(05,'Devendra', 'Shekhawat', 30000)

fetch_all_employee()



"""
There are numerous ORM implementations written in Python, including

    SQLAlchemy
    Peewee
    The Django ORM
    PonyORM
    SQLObject
    Tortoise ORM

"""

# Add code for SQL ALCHEMY ( object-relational mapper (ORM) )  and update the code for mlab







"""

Code Challenge 1
Write a python code to insert records to a mongo/sqlite/MySQL database named db_University for 10 students with fields like Student_Name, Student_Age, Student_Roll_no, Student_Branch.



Code Challenge 2

Perform similar steps as in the above code challenge but store the contents in an online mongo database named mLab.

https://mlab.com/home

https://docs.mlab.com/data-api/

"""


"""
# Best practice for making functions for INSERT, UPDATE, DELETE and SELECT and a class

Employee.py

class Employee :
"A sample Employee class"

def __init__(self, first, last, pay ) :
  self.first = first 
  self.last = last
  self.pay = pay

@property
def email(self) :
  return ‘{}.{}@email.com’.format(self.first,self.last)

@property
def fullname(self):
  return’{} {}’.format(self.first,self.last)

def __repr__(self):
  return “Employee(‘{}, ‘{}’, {})”.format(self.first,self.last,self.pay)


db.py

from employee import Employee 
emp_1 = Employee (‘John’, ‘Doe’, 80000)
emp_2 = Employee (‘Jane’, ‘Doe’, 90000)

print (emp_1.first)
print (emp_1.pay)
print (emp_1.last)

c.execute( “INSERT INTO employees VALUES ( ?, ?, ?)”, (emp_1.first,emp_1.last,emp_1.pay ) )

## or better way 

c.execute ("INSERT INTO employees VALUE (:first,:last,:pay)”, {‘first’:emp_1.first}, {‘last’:emp_1.last}, {‘pay’:emp_1.pay})

# we need a comma to specify it as tuple..it looks strange
c.execute(“SELECT * FROM employees WHERE last = ? ”, (’Schafer’, ) )

# or better way 
c.execute(“SELECT * FROM employees WHERE last = :last”,{‘last’:’Doe'} )


def insert_emp(emp):
  pass

def get_emps_by_name(lastname):
  pass

def update_pay ( emp, pay ):
  pass

def remove_emp(emp):
  pass

"""





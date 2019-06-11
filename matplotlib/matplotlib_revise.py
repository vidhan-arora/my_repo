# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 16:42:35 2019

@author: lenovo
"""

import matplotlib.pyplot as plt
x=[1,2,3,4,5,6]
y=[i for i in x*2]
y=[2,3,4,5,6,7]
plt.scatter(x,y)
plt.plot(x,y)
plt.grid(True)
plt.xlabel("marks")
plt.ylabel("attendance")
plt.title("marks and attendance ratio")
plt.plot(x,y,color="black")
plt.plot(x,y,'d',color="green")  #simple problem on plotting in matplotlib
#------------------------------------------------------------------------------
import matplotlib.pyplot as plt
sizes=[12,13,14,15]
explode=[0.1,0,0,0]
plt.pie(sizes,explode=explode,labels=['EE','ME','CSE','EC'],colors=['green','yellow','red','blue'],autopct='%1.1f%%')
plt.axis('equal')
plt.legend()
plt.plot()         #simple program with the help of matplotlib on oie chart
#------------------------------------------------------------------------------
import matplotlib.pyplot as plt
plt.bar([1,2,3,4,5],[4,3,6,1,9],align="center",alpha=0.5)
plt.xticks([1,2,3,4,5],['vidhan','piyush','arun','akshat','yash'])

#You can change the size of the plot by adding this

plt.rcParams["figure.figsize"] = [25,10]
plt.xlabel("name")

plt.title("name and nick number of person")
#------------------------------------------------------------------------------
import matplotlib.pyplot as plt
x1=[1,2,3,4,5]
y1=[3,6,5,8,9]
plt.plot(x1,y1,label="line1")
x2=[4,5,6,7,8]
y2=[4,6,1,2,6]
plt.plot(x2,y2,label="line2")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
#------------------------------------------------------------------------------import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[8,7,6,5,3]
plt.plot(x,y,label="vidhan",linestyle='dashed',linewidth=3,color='red',marker='o',markerfacecolor='blue',markersize=15)
plt.legend()
#------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np
def create_plot(ptype):
    np.arange(-10,10,0.01)
    if ptype=='linear':
         y=x
    elif ptype=='square':
         y=x**2
    elif ptype=='qubic':
         y=x**3
    elif ptype=='quadratic':
         y=x**4
    return(x,y)
plt.style.use("fivethirtyeight")
fig=plt.figure()
plt1=fig.add_subplot(334)
plt2=fig.add_subplot(332)
plt3=fig.add_subplot(331)
plt4=fig.add_subplot(333)
x,y= create_plot('linear')
plt1.plot(x,y,color='r')
plt1.set_title(' y_1 = x ')
x,y= create_plot('square')
plt2.plot(x,y,color='b')
plt2.set_title(' y_2 = x^2 ')
x,y= create_plot('qubic')
plt3.plot(x,y,color='g')
plt3.set_title(' y_3 = x^3 ')
x,y= create_plot('qudratic')
plt4.plot(x,y,color='y')
plt4.set_title(' y_4 = x^4 ')
fig.subplot_adjust(hspace=.5, wspace=0.5 )
plt.show()
#------------------------------------------------------------------------------
import matplotlib.pyplot as plt 
import numpy as np 
  

def create_plot(ptype): 
     
    x = np.arange(0, 5, 0.01) 
      
    
    if ptype == 'sin': 
    
        y = np.sin(2*np.pi*x) 
    elif ptype == 'exp': 
         
        y = np.exp(-x) 
    elif ptype == 'hybrid': 
    
        y = (np.sin(2*np.pi*x))*(np.exp(-x)) 
              
    return(x, y) 
  

plt.style.use('ggplot') 
  
 
plt1 = plt.subplot2grid((11,1), (0,0), rowspan = 3, colspan = 1) 
plt2 = plt.subplot2grid((11,1), (4,0), rowspan = 3, colspan = 1) 
plt3 = plt.subplot2grid((11,1), (8,0), rowspan = 3, colspan = 1) 
  

x, y = create_plot('sin') 
plt1.plot(x, y, label = 'sine wave', color ='b') 
x, y = create_plot('exp') 
plt2.plot(x, y, label = 'negative exponential', color = 'r') 
x, y = create_plot('hybrid') 
plt3.plot(x, y, label = 'damped sine wave', color = 'g') 
  

plt1.legend() 
plt2.legend() 
plt3.legend() 
  

plt.show()



















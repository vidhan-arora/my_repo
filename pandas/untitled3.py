# -*- coding: utf-8 -*-
"""
Created on Wed May 22 12:57:42 2019

@author: lenovo
"""

import matplotlib.pyplot as plt
list1 = [3,4,5,6,9,12]
list2 = [8,12,14,15,17,20]
plt.plot(list1, list2)
plt.savefig('fig1.png', dpi = 300)
plt.close()
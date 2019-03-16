# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 17:56:10 2019

@author: lenovo
"""

from collections import Counter
import numpy as np
a=(np.random.randint(5,15,40))
b=Counter(a)
print(b)#( without  numpy)

numpy,numpy1=np.unique(a,return_counts=True)
dict(zip(numpy,numpy1))#(with numpy)
















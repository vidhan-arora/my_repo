# -*- coding: utf-8 -*-
"""
Created on Wed May 22 08:40:27 2019

@author: lenovo
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def frame_filter(dataframe_col,year_repl):
    dataframe_col=pd.dataframe(dataframe_col[year_repl].dropna())
    dataframe_col_re=dataframe_col[year_repl].str.split(",",expand=True).add_prefix("col")
    dataframe_col_re.iloc[:,-1]=dataframe_col_re.iloc[:,-1].apply(int)
    female_data= dataframe_col_re[dataframe_col_re["col_1"]=="F"].sort_values("col_2",ascending=False).head()
    male_data= dataframe_col_re[dataframe_col_re["col_1"]=="M"].sort_values("col_2",ascending=False).head()
    sum_year= dataframe_col_re["col_2"].sum()
    gender_sum=pd.pivot_table(dataframe_col_re,values=['col_2'],column=["col_1"],aggfunc=np.sum)
    plt.pie([gender_sum["F"],gender_sum["M"]],explode=[0,0],labels=["female","male"],autopct="%1.1f%%")
    plt.axis("equal")
    return plt.show()
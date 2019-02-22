# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 18:55:53 2019

@author: lenovo
"""
import requests
url="https://free.currencyconverterapi.com/api/v6/convert?q=USD_PHP&compact=ultra&apiKey=8d235822bad9f7e1548b"
response=requests.get(url)
data=response.json()
print(data)
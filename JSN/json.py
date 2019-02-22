# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 13:04:13 2019

@author: lenovo
"""
import requests 
url="http://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b6907d289e10d714a6e88b30761fae22"
response= requests.get(url)
data=response.json()
print(response.text)
print(data["coord"])
print(data["sys"])
print(data["weather"])
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 16:58:54 2019

@author: lenovo
"""
from PIL import Image
img=Image.open("vidhan.jpg")
print(img.info)
print(img.size)
print(img.format)
img.show()
img_rotate=img.rotate(90)
img_rotate.show()
img_flip=img.transpose(Image.FLIP_TOP_BOTTOM)
img_flip.show()
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 15:09:22 2022

@author: Deepa Bhoomas Baskar
"""

def convertWeightToLbs(weight):
    Lbs= weight*2.20462
    return Lbs

def convertKgstoonces(weight):
    onces= weight*35.274
    return onces

for i in range (0,101,5):
     lbs= convertWeightToLbs(i)
     oc= convertKgstoonces(i)
     print("The coversion of", i, " in kg to lbs is= " ,lbs)
     print("The coversion of", i," in kg to ounces is= " ,oc)
     print("-------------------------------------------------------------")

     
        
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 17:53:16 2017

@author: Chiranjeev
"""

import  pandas as pd
XYZ_web = {'Day':[1,2,3,4,5,6],"Visitors":[1000,6000,500,1000,4900,800],"Bounce_Rate":[20,20,25,29,10,42]}
df = pd.DataFrame(XYZ_web)
print (df)
print (df.sum())
print (df.to_csv())
print (df.duplicated())
print (df.max())
##Slicing 
print(df.head(2))
print(df.tail(2))

##Mearging


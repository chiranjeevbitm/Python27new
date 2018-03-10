# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 17:53:16 2017

@author: Chiranjeev
"""

import  pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use("fivethirtyeight")
df = pd.DataFrame({'Day':[1,2,3,4,5,6],"Visitors":[10,60,50,30,49,22],"Bounce_Rate":[20,20,25,29,10,42]})

df.set_index("Day",inplace = True)
df.plot()
plt.title("Data Ploting")

plt.show()


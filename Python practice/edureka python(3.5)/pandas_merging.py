# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 18:12:20 2017

@author: Chiranjeev
"""

import pandas as pd
df1 = pd.DataFrame({"HPI":[80,90,70,60],"Int_rate":[2,1,2,3],"IND_GDP":[50,45,45,67]},
                    index = [2001,2002,2003,2004])

df2 = pd.DataFrame({"HPI":[80,90,70,60],"Int_rate":[2,1,2,3],"IND_GDP":[50,45,45,67]},
                    index = [2001,2002,2003,2005])

merge = pd.merge(df1,df2, on = "HPI")

print (merge)
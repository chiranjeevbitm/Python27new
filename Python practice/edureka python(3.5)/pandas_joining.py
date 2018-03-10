
"""
Created on Sat Dec 30 18:12:20 2017

@author: Chiranjeev
"""

import pandas as pd
df1 = pd.DataFrame({"HPI":[80,90,70,60],"rate":[2,1,2,3],"USA_GDP":[50,45,45,67]},
                    index = [2001,2002,2003,2004])

df2 = pd.DataFrame({"PPI":[80,90,70,60],"value":[2,1,2,3],"IND_GDP":[50,45,45,67]},
                    index = [2001,2002,2003,2005])

joined = df1.join(df2)

print (joined)
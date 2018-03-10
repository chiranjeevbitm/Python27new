# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 14:48:23 2017

@author: Chiranjeev
"""

from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')

x=[5,8,10]
y=[12,16,6]

x2=[6,9,11]
y2=[6,15,7]

plt.plot(x,y,'g',label='line one',linewidth=5)

plt.plot(x2,y2,'c',label='line two',linewidth=10)

plt.title('Epic info')
plt.ylabel('Y axis')
plt.xlabel('X axis')

plt.legend()
plt.grid(True,color='k')
plt.show()
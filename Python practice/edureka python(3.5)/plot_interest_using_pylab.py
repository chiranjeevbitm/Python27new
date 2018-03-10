# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 16:03:46 2017

@author: Chiranjeev
"""
import pylab

principal =10000
interestRate = 0.05
years = 20
values=[]
for i in range(years +1):
    values.append(principal)
    principal += principal * interestRate
pylab.plot(values)
    
pylab.title('5% growth , Compounded Annually')
pylab.xlabel('Years of compounding..')
pylab.ylabel('Values of principle ($)..')
pylab.show()
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 15:50:49 2017

@author: Chiranjeev
"""

import pylab
pylab.figure(1)
pylab.plot([1,2,3,4,5,6],[1,2,3,4,5,6])
pylab.figure(2)
pylab.plot([6,2,5,4,1,3],[1,2,3,4,5,6])
pylab.savefig('First Saved')
pylab.figure(1)
pylab.plot([5,7,6,10])
pylab.savefig('Second Saved')
pylab.show()

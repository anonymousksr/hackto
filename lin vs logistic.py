# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 09:31:42 2020

@author: Sarveswara Rao K
"""
'''
from math import exp
lin = [x/10 for x in range(0,11)]
log = [exp(x)/(1+exp(x)) for x in range(-5,6)]

#plot linear vs logistic
import matplotlib.pyplot as plt
#linear
plt.plot(range(0,11),lin,'green')
#logistic
plt.plot(range(0,11),log,'red')
#legend (markers)
plt.legend(['linear','logistic'])
#title
plt.title('Linear reg vs Logistic reg')
#Customisations done, display
plt.show()
'''

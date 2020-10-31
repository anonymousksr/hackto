# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 09:17:21 2020

@author: Sarveswara Rao K
"""

import pandas as pd
import numpy as np

da=pd.read_csv('Data.csv')

from sklearn.impute import SimpleImputer
imp=SimpleImputer()
x=da.iloc[:,:-1].values
y=da.iloc[:,-1].values
'''imp.fit(x[:,1:3])
x[:,1:3]=imp.transform(x[:,1:3])
'''
x[:,1:3]=imp.fit_transform(x[:,1:3])
from sklearn.preprocessing import LabelEncoder
lab=LabelEncoder()
y=lab.fit_transform(y)
x[:,0]=lab.fit_transform(x[:,0])
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
'''col = ColumnTransformer([('encoder',OneHotEncoder(),[0])],remainder='passthrough')
#x= np.array(col.fit_transform(x), dtype = np.str) 
x=col.fit_transform(x).toarray() '''
onehotencoder = OneHotEncoder() 
  
x = np.array(ColumnTransformer.fit_transform(x), dtype = np.str) 

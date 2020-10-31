# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 09:27:27 2020

@author: Sarveswara Rao K
"""
import pandas as pd
import numpy as np
data=pd.read_csv('USA_Housing.csv')

data.drop('Address',axis=1,inplace=True)
#import seaborn as sb
#sb.heatmap(data.corr(),annot=True)
x=data.iloc[:,:-1].values
y=data.iloc[:,-1].values

from sklearn.model_selection import train_test_split as tst
x_train,x_test,y_train,y_test=tst(x,y,test_size=0.3,random_state=43)
from sklearn.linear_model import LinearRegression as lr
logi=lr()
logi.fit(x_train,y_train)
logiacc=logi.score(x_test,y_test)
logipred=logi.predict(x_test)
from matplotlib import pyplot as plt
plt.scatter(y_test,logipred)
plt.show()

# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 09:35:35 2020

@author: Sarveswara Rao K
"""

import pandas as pd
import numpy as np
data=pd.read_csv('Iris.csv')
#data.info()
data=data.drop('Id',axis='columns')

#Data Interpretation

#data['Species'].value_counts()
#countplot for knowing the nubet pf species
'''import seaborn as sb
#1 
sb.countplot(x='Species',data=data)
#2 
sb.countplot(data['Species'])
# scatter plot to see feature to feature relation using pandas
pd.plotting.scatter_matrix(data,alpha=0.7,c='r',marker='S', markersizefigsize=(10,10))
from matplotlib import pyplot as plt
colors=(1,0,0)
plt.scatter(data['SepalLengthCm'],data['PetalWidthCm'],data['SepalLengthCm'],data['PetalLengthCm'],data['Species'],c=colors, alpha=1)
plt.show()'''

# replacing categorical data to numerical
data['Species'].unique()
classes={'Iris-setosa':0,'Iris-versicolor':1,'Iris-virginica':2}
data=data.replace({'Species':classes})
x=data.iloc[:,:-1].values
y=data.iloc[:,-1].values
from sklearn.model_selection import train_test_split as tts
x_train, x_test, y_train, y_test = tts(x,y,test_size=0.3,random_state=25)
from sklearn.linear_model import LogisticRegression as lr
logi=lr()
logi.fit(x_train,y_train)
logregacc=logi.score(x_test, y_test)
logregpred=logi.predict(x_test)

#Accuracy: confusion matrix

from sklearn.metrics import confusion_matrix as cm
da=cm(y_test,logregpred)

from sklearn.neighbors import KNeighborsClassifier as knn
knn1=knn()

knn1.fit(x_train,y_train)
knnpred=knn1.predict(x_test)
knnacc=knn1.score(x_test,y_test)

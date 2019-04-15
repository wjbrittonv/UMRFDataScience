#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, ShuffleSplit, cross_validate,cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn import metrics, svm
from sklearn.metrics import accuracy_score
from sklearn import preprocessing
from sklearn import tree
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from scipy.stats import chisquare
import seaborn
from matplotlib import pyplot
import matplotlib.pyplot as plt
from matplotlib import rcParams
from sklearn.cluster import KMeans, DBSCAN
from sklearn.feature_selection import chi2, SelectKBest, SelectFdr
from sklearn.decomposition import PCA
from rake_nltk import Rake


# In[1]:


df = pd.read_csv('problems_2categories_atprobcreation.csv')
# X = df.drop('Category', axis=1).values
# X
# le = preprocessing.LabelEncoder()
# for col in range(len(X[0])):
#     X[:,col] = le.fit_transform(X[:,col])
X = df.drop('Category', axis=1)
X = pd.get_dummies(X, columns=["'Assignment group'", "'Business service'",
                               'Company', "'Created Time'", "'Created by'", 
                               "'Opened by'", 'Type'])
y = df['Category'].values
y


# In[ ]:


from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import *
from matplotlib import pyplot
from sklearn.metrics import adjusted_rand_score, silhouette_score

pca = PCA(n_components=4)

# features = df[ ['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth'] ]
Xfit = pca.fit_transform(X)
df['pca1'] = Xfit[ : , 0]
df['pca2'] = Xfit[ : , 1]
df['pca3'] = Xfit[ : , 2]
df['pca4'] = Xfit[ : , 3]

model = KMeans(n_clusters=3)
model.fit(X)
print('Adjusted_Rand:', adjusted_rand_score(model.labels_, df.Category))
print('Silhouette:', silhouette_score(X, model.labels_))
print('Total explained variance:', sum(pca.explained_variance_ratio_))
seaborn.relplot(x="pca1", y="pca2", hue='Category', data = df)
fig = pyplot.figure()
ax = fig.add_subplot(111, projection='3d')

x = df['pca1']
y = df['pca2']
z = df['pca3']


for name, group in df.groupby('Category'):
    ax.scatter(group.pca1, group.pca2, group.pca3, label=name)
    
pyplot.show()


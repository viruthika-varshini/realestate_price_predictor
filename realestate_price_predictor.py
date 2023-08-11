# -*- coding: utf-8 -*-
"""realestate_price_predictor.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1G7PnzPxSW4OKU7C_JP2x0__nZWShprGW
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn import preprocessing

df = pd.read_csv('/content/Real estate.csv')
df.head()

df.shape

df.drop('No',inplace= True, axis= 1)

df.shape

df.columns.values

#Step 3: Create a scatterplot to visualize the data
sns.scatterplot(x='X4 number of convenience stores',
                y='Y house price of unit area', data= df)

# Step 3b addition----univariate analysis vs Price of Unit Area---->
sns.scatterplot(x = 'X3 distance to the nearest MRT station',
               y='Y house price of unit area', data = df)

# 'X2 house age'
sns.scatterplot(x = 'X2 house age', y='Y house price of unit area',data = df)

#creating a feature variables
X= df.drop('Y house price of unit area',axis= 1)
y= df['Y house price of unit area']
X

y

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,random_state= 3)

lr = LinearRegression()
lr.fit(X_train, y_train)
predictions = lr.predict(X_test)

print("R2 score", r2_score(y_test,predictions))
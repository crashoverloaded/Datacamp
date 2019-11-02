#!/usr/bin/python3

from sklearn import datasets
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
# Using GGplot as it is very Good in visuals
plt.style.use('ggplot')

# Loading IRIS dataset
iris = datasets.load_iris()

# Loading Data or Features
X = iris.data

# Loading Target or Result
Y = iris.target

# Bulding Dataframe
df = pd.DataFrame(X,columns=iris.feature_names)

# printing first 5 rows 
print(df.head())

# Visualising EDA(Exploratory Data Analysis)
# "c=y" for color target variable(colored species) , "s" is shape and "marker" is marker size
_ = pd.plotting.scatter_matrix(df, c=Y, figsize = [8,8] , s=150,marker = 'D')
plt.show()

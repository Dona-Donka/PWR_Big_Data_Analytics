# https://www.kaggle.com/c/boston-housing
# https://towardsdatascience.com/linear-regression-on-boston-housing-dataset-f409b7e4a155

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

#l load dataset from scikit-learn
from sklearn.datasets import load_boston
boston_dataset = load_boston()

print(boston_dataset.keys())
# dict_keys(['data', 'target', 'feature_names', 'DESCR', 'filename'])
# 'data' - contains the info for various houses
# 'target' - prices of the house
# 'feature_names' - names of the features
# 'DESCR' - describes the dataset

# print more about the dataset
print(boston_dataset.DESCR)

# load data into pandas dataframe
boston = pd.DataFrame(boston_dataset.data, columns=boston_dataset.feature_names)
print(boston.head())

# Prepare the data for training the mode
boston["PRICE"] = boston_dataset.target
boston.isnull().sum() # count the number of missing values

X = boston.drop('PRICE', axis=1)
Y = boston['PRICE']

# split the data into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state=5)
print("X_train: ", X_train.shape, "\n",
      "Y_train: ", Y_train.shape, "\n",
      "X_test: ", X_test.shape, "\n",
      "Y_test: ", Y_test.shape)

# X_train:  (404, 2)
# Y_train:  (404,)
# X_test:  (102, 2)
# Y_test:  (102,)

# plot regression
from sklearn.linear_model import LinearRegression
linearRegression = LinearRegression()
linearRegression.fit(X_train, Y_train)

Y_pred = linearRegression.predict(X_test)

plt.scatter(Y_test, Y_pred)
plt.xlabel("Prices")
plt.ylabel("Predicted prices")
plt.title("Boston houses prices")
plt.savefig('DL_hw1.png')


# compute mean squared error
# https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html
from sklearn.metrics import mean_squared_error

# number of samples : [102, 404] - it not works
meanSquaredError = mean_squared_error(Y_test, Y_train)
print("mean squared error: ", meanSquaredError)

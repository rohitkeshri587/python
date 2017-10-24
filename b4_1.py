import pandas as pd
import numpy as np
import seaborn as sns
from pandas import Series, DataFrame
import matplotlib.pyplot as plt 

titanic_df = pd.read_csv("mytrain.csv")

print("======Data Headers=======")
titanic_df.head()

print("=====Data Description=====")
titanic_df.info()
titanic_df.describe()

titanic_df = titanic_df.drop(['PassengerId', 'Name', 'Ticket'], axis=1)

titanic_df.drop(['Parch'], axis=1, inplace=True)

print("=====Check if columns were really dropped=====")
titanic_df.head()

titanic_df["Embarked"] = titanic_df["Embarked"].fillna("S")
print(titanic_df["Embarked"])

print("Number of rows in the data frame is ",len(titanic_df))

print("Number of columns in the data frame is ",len(titanic_df.columns))

print("Minimum Age is", titanic_df.Age.min())
print("Maximum Age is", titanic_df.Age.max())

print ("Mean value of Age is", titanic_df.Age.mean())
print("Std Deviation of Age is", titanic_df.Age.std())

titanic_df.Age.hist()
plt.show()

ax1= titanic_df.Age.hist()
ax1.set(xlabel='Age', ylabel='Number of people')
plt.show()

ax2= titanic_df.Age.plot()
plt.show()

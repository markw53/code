# import pandas library
import pandas as pd

# read in a file and assign to variable df
df = pd.read_csv("D:\OneDrive\Downloads\pandas data.csv")

# outputs the top 10
#print(df.head(10))

# outputs the last 10
#print(df.tail(10))

# outputs whole data frame
#print(df)

# prints rows and columns are in the data frame
#print(df.shape)

# outputs data types
#print(df.info())

# outputs column headings
#print(df.columns)

# outputs statistical distribution by column
#print(df.describe())

# checks for any null values
#print(df.isnull().any())

# outputs how many missing values in each column
#print(df.isnull().sum())

# outputs unique values for each category
#print(df["Distance"].unique())
#print(df["Pulse"].unique())
#print(df["Maxpulse"].unique())
#print(df["Calories"].unique())

# filter by calories in the data frame
#print(df[df["Calories"]>400])

# find the mode for a particular column
#y = df["Calories"].mode()
#print(y)

# finds the mean of the distance column and rounds to 1 d.p.
#x = df["Distance"].mean()
#x = round(x,1)
#print(x)

# function to replace 'NaN' in the data frame with previously calculated mean value
#df["Distance"] = df["Distance"].fillna(x)

# check to see distance column now has no null values
#print(df.isnull().sum())

# use numpy library to replace any value in the data frame
#from numpy import nan

# Calculate mean of calories column and replace NaN with that value
#y = df["Calories"].mean()
#y = round(y,1)
#print(y)

#df["Calories"] = df["Calories"].replace(to_replace = nan, value = y)

#print(df.isnull().sum())

# create new measure
#df["PulsePlus"] = df["Maxpulse"] - df["Pulse"]

#print(df)

import matplotlib.pyplot as plt
import numpy as np

x_axis = np.array([0,10])
y_axis = np.array([0,100])
plt.plot(x_axis, y_axis)
plt.show()




















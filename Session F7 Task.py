# import pandas library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# read in a file and assign to variable df
df = pd.read_csv("D:\OneDrive\Documents\Data Analytics Bootcamp\F - Python\mhs Data for F7.csv")
print(df)

# prints rows and columns are in the data frame
print(df.shape)

# outputs data types
print(df.info())

# outputs column headings
print(df.columns)

# outputs statistical distribution by column
print(df.describe())

# checks for any null values
print(df.isnull().any())

# outputs how many missing values in each column
print(df.isnull().sum())

# print unique values to help clean the data
print(df["Age"].unique())
print(df["SystolicBP"].unique())
print(df["DiastolicBP"].unique())
print(df["BS"].unique())
print(df["BodyTemp"].unique())
print(df["HeartRate"].unique())

# clean age
# replace text with number, replace nan with 0, convert to integer and find the mean
from numpy import nan
df["Age"] = df["Age"].replace(to_replace = "Twenty", value = 20)
df["Age"] = df["Age"].replace(to_replace = nan, value = 0)
df["Age"] = df["Age"].astype(int)
x = df["Age"].mean()
x = round(x,1)
print(x)

# replace 0 with the mean and check for null values
df["Age"] = df["Age"].replace(to_replace = 0, value = x)
print(df.isnull().sum())

# Repeat for SystolicBP
y = df["SystolicBP"].mean()
y = round(y,1)
print(y)

# correct anomaly in DiastolicBP
df["DiastolicBP"] = df["DiastolicBP"].replace(to_replace = 1000, value = 100)

# replace nulls with the mean
df["SystolicBP"] = df["SystolicBP"].replace(to_replace = nan, value = y)
print(df.isnull().sum())

# repeat for BodyTemp
z = df["BodyTemp"].mean()
z = round(z,1)
print(z)

# replace nulls with the mean
df["BodyTemp"] = df["BodyTemp"].replace(to_replace = nan, value = z)
print(df.isnull().sum())

print(df)

# clean HeartRate column
df["HeartRate"] = df["HeartRate"].replace(to_replace = "Seventy", value = 70)
df["HeartRate"] = df["HeartRate"].astype(int)
w = df["HeartRate"].mean()
w = round(w,1)
print(w)

df["HeartRate"] = df["HeartRate"].replace(to_replace = 7, value = w)

print(df.info())
print(df.isnull().sum())

# remove everyone under 16 as they should not be pregnant!
df = df[df["Age"] > 16]
print(df)

# create new measure to correct BS recording
df["BSNew"] = df["BS"] + 3
print(df)

# correlation matrix
df2 = df[["Age", "SystolicBP", "DiastolicBP", "BSNew", "BodyTemp", "HeartRate"]].copy()
corrmax = df2.corr()
print(corrmax)

# plot visuals
plt.scatter(df["Age"],df["BSNew"], label = "Blood Sugar", color = "red")
plt.xlabel("Age")
plt.ylabel("Blood Sugar")
plt.title("Maternal Health of Women in pregnancy")
plt.legend()
plt.show()

plt.scatter(df["SystolicBP"], df["DiastolicBP"], label = "Blood Pressure", color = "red")
plt.xlabel("Systolic")
plt.ylabel("Diastolic")
plt.show()

# histogram of ages
data = df["Age"]
plt.hist(data, bins = 20, color = "skyblue", edgecolor = "black")
plt.xlabel("Ages")
plt.ylabel("Frequency")
plt.title("Histogram of ages")
plt.show()

plt.scatter(df["Age"],df["HeartRate"], label = "Heart Rate Sugar", color = "red")
plt.xlabel("Age")
plt.ylabel("Heart Rate")
plt.title("Maternal Health of Women in pregnancy")
plt.legend()
plt.show()

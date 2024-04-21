# import pandas library
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# read in a file and assign to variable df
df = pd.read_csv("D:\OneDrive\Downloads\pandas data.csv")

# create graph with x and y axis
#x_axis = np.array([0,10])
#y_axis = np.array([0,100])
#plt.plot(x_axis, y_axis)
#plt.show()

# subplot 1
x_axis = np.array([1,3,6,8,10])
y_axis = np.array([1,5,6,3,12])
plt.plot(x_axis, y_axis, linestyle = 'dotted', color = "red")
plt.title("Exercise Readings")
plt.xlabel("Pulse")
plt.ylabel("Calories")
plt.subplot(1,1,1)
plt.grid()
plt.show()

# subplot 2
x_axis = np.array([4,1,6,8,15])
y_axis = np.array([6,5,6,7,10])
plt.plot(x_axis, y_axis, linestyle = 'dotted', color = "red")
plt.title("Exercise Readings")
plt.xlabel("Pulse")
plt.ylabel("Calories")
plt.subplot(1,1,1)
plt.grid()
plt.show()

# plot a scatter graph
x_axis = np.array([1,3,6,8,10,2,10,5,7,8,3,5])
y_axis = np.array([1,5,6,3,12,5,5,8,10,6,3,6])
plt.scatter(x_axis, y_axis,)
plt.title("Exercise Readings")
plt.xlabel("Pulse")
plt.ylabel("Calories")
plt.grid()
plt.show()

# plot a bar graph
x_axis = np.array(['Pen', 'Pencil', 'Paper', 'Marker'])
y_axis = np.array([10, 30, 10, 15])
plt.bar(x_axis, y_axis)
plt.title('Items Sales')
plt.xlabel('Item')
plt.ylabel('Quantity')
plt.show()

# plot a histogram
x_axis = np.array([100,10,200])
plt.hist(x_axis)
plt.title("Items Sales")
plt.xlabel("Item")
plt.ylabel("Quantity")
plt.show()

# plotting
plt.figure(figsize=(10,6))

# scatter plot for Pulse and Maxpulse
plt.scatter(df["Distance"], df["Pulse"], label = 'Pulse', color = 'blue')
plt.scatter(df["Distance"], df["Maxpulse"], label = 'Maxpulse', color = 'red')

# line plot for calories
#plt.plot(df["Distance"], df["Calories"], label = "Calories", linestyle = "--", marker = "o", color = "green")

# adding labels and title
plt.xlabel('Distance')
plt.ylabel('Values')
plt.title('Fitness Dataset')
plt.legend()

# Show the plot
plt.show()






#Importing Matplotlib module
import matplotlib.pyplot as plt
squares = [1,4,13,25,33]

input_values = [1,2,3,4,5]
plt.scatter(2,4,s=200)
#Set Chart Title and axes
plt.title("Squares Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of label",fontsize=14)

#Set Size of Tick Tables
plt.tick_params(axis='both',which='major',labelsize=14)
plt.plot(input_values,squares,linewidth=5)
plt.show()

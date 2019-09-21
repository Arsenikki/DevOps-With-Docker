#%%
import matplotlib.pyplot as plt #define shorthand "plt" for package matlobplit.pyplot
import numpy as np #define shorthand "np" for the numpy package 

def example_func(x):
    f_x = 1/(1+np.exp(-x))
    return f_x

range_x = np.arange(-6 , 6 , 0.01)

f_x = np.empty(len(range_x))

for i in range(len(range_x)):
    f_x[i] = example_func(range_x[i])

### STUDENT TASK ###
#1) plot the results, for example use plot function in matplotlib.pyplot. Remember to show() the plot.
plt.show(plt.plot(range_x , f_x))

### STUDENT TASK ###
#2) find the first derivative of the mentioned function and plot it
# YOUR CODE HERE

a = np.gradient(f_x)
plt.show(plt.plot(range_x,a))

#%%

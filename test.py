import numpy as np
import matplotlib.pyplot as plt
import sympy
import math
import random
from scipy.interpolate import interp1d, lagrange


# data = [(1,9),(2,3),(3,5),(4,3),(7,1),(8,0)]
# x_data = [d[0] for d in data]
# y_data = [d[1] for d in data]
# x_min = x_data[0]
# x_max = x_data[-1]
# f1 = interp1d(x_data, y_data, kind='quadratic')
# f2 = interp1d(x_data, y_data, kind='cubic')
# #p = lagrange(x_data, y_data)
# xs = np.linspace(x_min, x_max, 200)
# y1 = f1(xs)
# y2 = f2(xs)
# plt.plot(x_data, y_data,'ok')
# plt.plot(xs,y1, '-')
# plt.plot(xs,y2, '--')
# plt.legend(['data', 'quadratic', 'cubic'], loc='best')
# plt.show()


#Create functions
x_vals = np.linspace(0.1,3,100)
y_quad = [x**2 + random.random()*0.1 for x in x_vals]
random.seed()
y_log = [math.log(x) + random.random()*0.1 for x in x_vals]
#plt.plot(x_vals, y_quad, '-')
#plt.plot(x_vals, y_log, '--')
plt.show()

def getRandomPoints(x_, y_, rand=0.7):
    """
    Goal:
        produce a subset of points from 2 arrays representing the x and y values of a function
    Inputs:
        x_ - an array of x values
        y_ - an array of y values
        rand - how many random values to select
    Output:
        x_, y_ - a subset of x and y values
    Note: 
        the first x value and last x value, that is the end points of the x interval [a,b] must be included in the random set
        for the interpolation function to work properly in the region [a,b]
    """

    random.seed()
    x_rand = []
    y_rand = []
    for i in range(len(x_)):
        if (i == 0 or i == len(x_) - 1 or random.random()>rand):
            x_rand.append(x_[i])
            y_rand.append(y_[i])
    
    return [x_rand, y_rand]

def calculateError(y_, y_pred):
    """
    Goal: given a predicted function find the RSS and the r^2 values to gauge accuracy of your model
    Inputs:
        y_      - "true" y values
        y_pred  - predicted y values
    Output:
        RSS -   residual sum squared
        r^2 -   ration of explained sum of squares to total sum squared (i.e. 1 - RSS/TSS)
    """
    RSS = 0
    TSS = 0
    y_mean = np.mean(y_)
    for i in range(len(y_)):
        RSS += (y_pred[i] - y_[i])**2
        TSS += (y_pred[i] - y_mean)**2
    
    return TSS, (1 - RSS/TSS)

    

#Choose some points at random from those functions

x_rand, y_rand = getRandomPoints(x_vals, y_quad)
f1 = interp1d(x_rand, y_rand, kind='linear')
plt.plot(x_vals, y_quad, '-')
ys = f1(x_vals)
rss, r_s = calculateError(y_quad, ys)
print("rss: ", rss, " r^2: ", r_s)
plt.plot(x_vals, ys)
plt.title("r^2=%.4f" % r_s)
plt.legend(['quadratic', 'linear_interp'], loc='best')
plt.show()

x_rand, y_rand = getRandomPoints(x_vals, y_log)
f2 = interp1d(x_rand, y_rand, kind='linear')
f3 = interp1d(x_rand, y_rand, kind='quadratic')
plt.plot(x_vals, y_log)
plt.plot(x_vals, f2(x_vals), '--')
plt.plot(x_vals, f3(x_vals))
plt.legend(['log', 'linear_interp', 'quadratic_interp'], loc='best')
plt.show()




